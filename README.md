# Weather Data ETL Pipeline

A concise, end-to-end pipeline that ingests, cleans, and stores hourly weather observations for analysis and visualization. This repository focuses on reproducibility and clear documentation to make the project easy to run and share.

Overview
- Purpose: demonstrate a complete ETL workflow for time-series weather data using Python, Docker, and CI.
- Components: data fetcher, basic cleaning/transformation, local storage (CSV/parquet), and a simple plotter for quick inspection.

Quick start (local)
1. Clone:
   git clone https://github.com/LokeshwarReddy-DS/Weather-Data-ETL-Pipeline
   cd Weather-Data-ETL-Pipeline
2. Create virtual environment and install:
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
3. Run demo:
   python examples/run_demo.py --lat 40.71 --lon -74.01 --start 2025-01-01 --end 2025-01-02

Run with Docker Compose
- docker-compose up --build

Project structure
- src/           # core ETL modules (keep code modular and importable)
- examples/      # runnable example script and generated outputs
- tests/         # pytest tests
- diagrams/      # optional architecture diagrams (add images)
- docker-compose.yml
- requirements.txt

Development
- Test: pytest
- Lint: ruff
- Prefer type hints on public functions

License
- MIT

Contact
- Lokeshwar Reddy — GitHub: @LokeshwarReddy-DS
