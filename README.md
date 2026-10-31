
# Smart Hospital Data Platform

## Project Overview

The Smart Hospital Data Platform is a data engineering project designed to collect, clean, store, and analyze hospital data.

The initial version focuses on the Emergency Department and provides useful indicators to support hospital operations.

## Technologies Used

- Python
- PostgreSQL
- SQL
- Git and GitHub

## Project Architecture

CSV Data
   |
   v
Python ETL Pipeline
   |
   v
Data Validation and Cleaning
   |
   v
PostgreSQL Database
   |
   v
SQL Analytics

## Project Structure

```text
smart-hospital-data-platform/
├── data/
├── src/
│   ├── main.py
│   └── database.py
├── sql/
│   └── analysis.sql
├── tests/
│   └── test_main.py
├── .gitignore
└── README.md
```

## Key Features

- CSV data extraction
- Data validation and cleaning
- Waiting time calculation
- PostgreSQL database integration
- Automated data loading
- SQL analytics
- Python unit testing

## Hospital Analytics

The platform analyzes:

- Emergency visits by urgency level
- Average waiting time by urgency
- Cases by diagnosis category
- Patient outcomes

## Future Improvements

- Add more hospital departments
- Implement Apache Airflow
- Introduce dbt for data transformations
- Build interactive dashboards with Power BI
- Add Docker support

## Author

Abderrahmane Ashoubi
