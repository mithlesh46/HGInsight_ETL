import logging
from concurrent.futures import ThreadPoolExecutor


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(name)s %(message)s',
    )


def get_thread_pool(max_workers=4):
    return ThreadPoolExecutor(max_workers=max_workers)
