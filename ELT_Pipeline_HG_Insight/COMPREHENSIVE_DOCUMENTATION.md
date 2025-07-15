# ELT_Pipeline_HG_Insight - Comprehensive Documentation

## Table of Contents
1. [Overview](#overview)
2. [Architecture & Workflow](#architecture--workflow)
3. [Repository Structure](#repository-structure)
4. [Setup & Installation](#setup--installation)
5. [Configuration](#configuration)
6. [Running the Pipeline](#running-the-pipeline)
7. [Orchestration](#orchestration)
8. [Reporting & Analytics](#reporting--analytics)
9. [PII Anonymization](#pii-anonymization)
10. [Testing](#testing)
11. [Extending the Pipeline](#extending-the-pipeline)
12. [Troubleshooting](#troubleshooting)
13. [License](#license)

---

## 1. Overview

**ELT_Pipeline_HG_Insight** is a production-grade, modular, and containerized ELT (Extract, Load, Transform) pipeline designed for ingesting, processing, and reporting on customer churn data. It features robust error handling, PII anonymization, orchestration (cron & Airflow), and seamless integration with Metabase for analytics.

---

## 2. Architecture & Workflow

**High-Level Steps:**
1. **Extract:** Ingests CSV data from the `Data/` directory.
2. **Load (Staging):** Loads raw data into a staging table in SQLite.
3. **Transform:**
   - Handles missing values using configurable defaults.
   - Anonymizes PII columns (e.g., Name, Email) using the Faker library.
   - Uses multithreading for performance.
4. **Load (Reporting):** Loads processed data into a reporting table for analytics.
5. **Orchestration:**
   - Can be run manually, on a schedule (cron), or via Airflow for enterprise workflows.
6. **Reporting:**
   - Metabase connects to the reporting database for dashboarding and analytics.

---

## 3. Repository Structure

```
ELT_Pipeline_HG_Insight/
├── Data/                  # Input data files (CSV)
├── elt/                   # Modular ELT code (extract, load, transform, etc.)
├── tests/                 # Unit and integration tests
├── docker/                # Docker and orchestration files
├── airflow/               # Airflow DAGs and config (for advanced orchestration)
├── pipeline.py            # Main pipeline runner
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
├── .gitignore             # Ignore patterns
├── README.md              # Quick start and usage
└── COMPREHENSIVE_DOCUMENTATION.md # This file
```

---

## 4. Setup & Installation

### Local Development
1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd ELT_Pipeline_HG_Insight
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Dockerized Setup
1. **Build and run with Docker Compose:**
   ```bash
   cd docker
   docker-compose up --build
   ```
2. **All services (pipeline, Metabase, etc.) will start in containers.**

---

## 5. Configuration

- All configuration is managed via the `.env` file:
  ```ini
  DATA_PATH=Data/customer_churn_data.csv
  DB_URL=sqlite:///elt_pipeline.db
  STAGING_TABLE=staging
  REPORTING_TABLE=reporting
  PII_COLUMNS=Name,Email
  MISSING_DEFAULTS={"Name": "Unknown", "Email": "unknown@example.com", "Age": 0}
  ```
- Adjust these values as needed for your data and environment.

---

## 6. Running the Pipeline

### Manually (Local)
```bash
python pipeline.py
```

### In Docker (One-off Run)
```bash
docker-compose run --rm elt-pipeline python pipeline.py
```

---

## 7. Orchestration

### Cron-based (Default in Docker)
- The pipeline runs every hour via cron inside the container.
- To change the schedule, edit `docker/elt_cron`.

### Airflow-based (Enterprise Option)
- Airflow services and a sample DAG are included for advanced scheduling and monitoring.
- To enable, uncomment Airflow services in `docker-compose.yml` and start the stack.
- Access Airflow UI at [http://localhost:8080](http://localhost:8080).

---

## 8. Reporting & Analytics

- **Metabase** is included for BI and dashboarding.
- Access Metabase at [http://localhost:3000](http://localhost:3000).
- Connect to the SQLite database at `/app/elt_pipeline_data/elt_pipeline.db`.
- Build dashboards and explore the processed data in the `reporting` table.

---

## 9. PII Anonymization

- PII columns (e.g., Name, Email) are specified in `.env` via `PII_COLUMNS`.
- The pipeline uses the Faker library to replace real PII with fake values.
- This ensures privacy and compliance with data protection standards.
- If no PII columns are present in the data, this step is skipped.

---

## 10. Testing

- Unit and integration tests are in the `tests/` directory.
- Run all tests with:
  ```bash
  pytest tests
  ```
- Tests cover extraction, loading, transformation, and the full pipeline.

---

## 11. Extending the Pipeline

- **Swap databases:** Change `DB_URL` in `.env` to use Postgres or MySQL.
- **Add new transformations:** Extend `elt/transform.py` with new methods.
- **Add new data sources:** Implement new extractors in `elt/extract.py`.
- **Add more reporting:** Build new dashboards in Metabase.
- **Integrate with CI/CD:** Add GitHub Actions for automated testing.

---

## 12. Troubleshooting

- **Missing dependencies:** Ensure your virtual environment is activated and dependencies are installed.
- **Database not found:** Check the path in `.env` and ensure the pipeline has run.
- **Metabase not connecting:** Ensure the Docker volume is mounted and the path is correct.
- **PII not anonymized:** Ensure columns exist in the data and are listed in `PII_COLUMNS`.

---

## 13. License

This project is open source and available under the MIT License. 