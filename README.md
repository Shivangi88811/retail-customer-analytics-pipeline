# Retail Customer Analytics Pipeline

## Project Overview

This project demonstrates an end-to-end modern Analytics Engineering and Data Engineering workflow using real-world retail e-commerce data.

The pipeline ingests raw retail datasets, loads them into a DuckDB warehouse, transforms the data using dbt, models analytics-ready marts using dimensional modeling principles, and visualizes business insights through Tableau dashboards.

The project simulates enterprise-style analytics architecture commonly used in modern data platforms.

---

# Business Problem

Retail and e-commerce organizations generate large amounts of transactional and customer data from multiple operational systems.

Business teams require:
- clean analytics-ready datasets
- customer revenue insights
- payment analytics
- geographic performance analysis
- KPI dashboards
- scalable transformation pipelines

This project demonstrates how raw operational data can be transformed into business-ready analytics models using modern ELT architecture.

---

# Architecture

```text
Raw Retail CSV Data         
        ↓
Python Ingestion Pipeline
        ↓
DuckDB Data Warehouse
        ↓
dbt Staging Models
        ↓
Fact & Dimension Tables
        ↓
Analytics Marts
        ↓
Tableau Dashboards
```

---

# Technology Stack

| Layer | Technology |
|---|---|
| Programming | Python |
| Data Processing | Pandas |
| Data Warehouse | DuckDB |
| Transformations | dbt |
| Data Modeling | Star Schema |
| Visualization | Tableau Public |
| Version Control | Git & GitHub |

---

# Project Workflow

## 1. Data Ingestion
- Loaded multiple retail datasets using Python and Pandas
- Performed schema inspection and profiling
- Validated missing values and dataset integrity

## 2. Warehouse Loading
- Loaded datasets into DuckDB warehouse tables
- Created relational warehouse structure

## 3. dbt Transformations
Created modular dbt models including:
- staging models
- fact tables
- dimension tables
- analytics marts

## 4. Dimensional Modeling
Implemented star schema architecture:
- fct_orders
- dim_customers
- customer_revenue_mart

## 5. Business Intelligence
Built Tableau dashboards for:
- revenue analysis
- customer analytics
- geographic trends
- payment insights
- executive KPI reporting

---

# dbt Models

## Staging Models
- stg_customers
- stg_orders
- stg_payments

## Fact Tables
- fct_orders

## Dimension Tables
- dim_customers

## Analytics Marts
- customer_revenue_mart

---

# Tableau Dashboard Features

The Tableau dashboards provide:

- Executive KPI reporting
- Revenue analysis
- Customer segmentation insights
- Geographic revenue distribution
- Order analytics
- Payment method analysis

---

# Key Analytics KPIs

- Total Revenue
- Total Orders
- Average Order Value
- Revenue by State
- Revenue by Customer City
- Customer Revenue Distribution

---

# Data Engineering Concepts Demonstrated

- ELT architecture
- Multi-file ingestion
- Warehouse modeling
- dbt transformations
- Star schema design
- Fact and dimension modeling
- Analytics marts
- Data quality testing
- BI reporting workflows

---

# Future Enhancements

Planned future improvements include:
- Apache Airflow orchestration
- Incremental dbt models
- AI-generated business summaries
- Anomaly detection
- Customer segmentation modeling
- Real-time ingestion pipelines
- Cloud warehouse migration
- Advanced analytics dashboards

---

# Project Structure

text retail-customer-analytics-pipeline/ │ ├── app/ │   ├── ingestion.py │   └── dashboard.py │ ├── data/ │   ├── raw/ │   └── processed/ │ ├── retail_analytics_dbt/ │   ├── models/ │   │   ├── staging/ │   │   └── marts/ │ ├── notebooks/ ├── docs/ ├── sql/ │ ├── README.md └── requirements.txt 

---

# How To Run

## Clone Repository

bash git clone <repo-url> 

## Install Dependencies

bash pip install -r requirements.txt 

## Run Ingestion Pipeline

bash python3 app/ingestion.py 

## Run dbt Models

bash cd retail_analytics_dbt  dbt run 

## Run dbt Tests

bash dbt test 

---

# Dataset

Dataset source:
Brazilian E-Commerce Public Dataset by Olist

---

# Author

Shivangi Ajmeri
