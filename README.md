# CSV Ingestion Pipeline

A simple data engineering pipeline that ingests CSV customer data, performs validation and cleaning, loads records into DuckDB, and generates summary analytics using SQL.

## Features

- CSV ingestion
- Duplicate record removal
- Missing value handling
- DuckDB warehouse loading
- SQL aggregation queries
- Basic analytics reporting

## Tech Stack

- Python
- Pandas
- DuckDB

## Pipeline Workflow

CSV File
↓
Python Ingestion
↓
Data Cleaning & Validation
↓
DuckDB Warehouse
↓
SQL Aggregation
↓
Analytics Output

## Run Project

```bash
python app.py