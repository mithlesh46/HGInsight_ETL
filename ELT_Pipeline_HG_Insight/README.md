# ELT_Pipeline_HG_Insight

## Problem Statement

1. Create an ELT pipeline that ingests a CSV dataset available in Data folder.
2. Load up the dataset into a staging database of your choice.
3. Design a transformation layer to process the input dataset for missing values (use defaults) and anonymising PII.
4. The destination for the processed data should be a database ideal for generating reports.
5. Establish an orchestration workflow for this pipeline to accept a feed every hour (should be configurable).
6. Integrate any open-source reporting tool to generate statistics about the flow.
7. Ensure the entire setup is available through composable container definition(s).

## Tech Stack

- Python 3.12
- Pandas, SQLAlchemy, Faker, python-dotenv
- SQLite (default, can be swapped for Postgres/MySQL)
- Metabase (open-source reporting, via Docker)
- Docker & Docker Compose

## Repository Structure

```
ELT_Pipeline_HG_Insight/
├── Data/                  # Input data files (CSV)
├── elt/                   # Modular ELT code (extract, load, transform, etc.)
├── tests/                 # Unit and integration tests
├── docker/                # Docker and orchestration files
├── pipeline.py            # Main pipeline runner
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
├── .gitignore             # Ignore patterns
└── README.md              # This file
```

## Setup & Usage

### 1. Local Development

#### a. Install dependencies (recommended: use a virtual environment)
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### b. Configure environment variables
Edit `.env` as needed (defaults provided):
```
DATA_PATH=Data/customer_churn_data.csv
DB_URL=sqlite:///elt_pipeline.db
STAGING_TABLE=staging
REPORTING_TABLE=reporting
PII_COLUMNS=Name,Email
MISSING_DEFAULTS={"Name": "Unknown", "Email": "unknown@example.com", "Age": 0}
```

#### c. Run the pipeline
```bash
python pipeline.py
```

#### d. Run tests
```bash
pytest tests
```

### 2. Dockerized Setup (Recommended for Production)

#### a. Build and run with Docker Compose
```bash
cd docker
docker-compose up --build
```
- This will run the ELT pipeline and launch Metabase (http://localhost:3000)
- The SQLite database is persisted in a Docker volume.

#### b. Access Metabase
- Open [http://localhost:3000](http://localhost:3000) in your browser.
- On first login, set up an admin user.
- Connect to the SQLite database at `/app/elt_pipeline_data/elt_pipeline.db` (Metabase should auto-detect it).
- Build dashboards and explore your processed data!

### 3. Scheduling the Pipeline
- By default, the pipeline runs once per container start.
- For hourly or custom scheduling, use cron or a workflow orchestrator (e.g., Airflow) in production.
- Example: Add a cron job in the Dockerfile or use a workflow tool.

## Customization
- Swap out SQLite for Postgres/MySQL by changing `DB_URL` in `.env` and updating Docker Compose.
- Adjust PII columns and missing value defaults in `.env`.