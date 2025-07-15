from elt.extract import Extractor
from elt.load import Loader
from elt.transform import Transformer
from elt.config import Config
from elt.utils import setup_logging, get_thread_pool
import logging


def run_pipeline():
    setup_logging()
    logger = logging.getLogger("pipeline")
    config = Config()

    extractor = Extractor(config.data_path)
    loader = Loader(config.db_url)
    transformer = Transformer()

    # Extract
    df = extractor.extract()
    if df is None:
        logger.error("Extraction failed. Exiting pipeline.")
        return

    # Load to staging
    if not loader.load_to_staging(df, config.staging_table):
        logger.error("Loading to staging failed. Exiting pipeline.")
        return

    # Transform (multithreaded: missing values and PII anonymization)
    with get_thread_pool(max_workers=2) as pool:
        future_missing = pool.submit(transformer.handle_missing, df, config.missing_defaults)
        df_missing = future_missing.result()
        future_pii = pool.submit(transformer.anonymize_pii, df_missing, config.pii_columns)
        df_transformed = future_pii.result()

    # Load to reporting
    if not loader.load_to_reporting(df_transformed, config.reporting_table):
        logger.error("Loading to reporting failed. Exiting pipeline.")
        return

    logger.info("Pipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()
