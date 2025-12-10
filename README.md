Crypto Price ETL

A simple end-to-end ETL pipeline that fetches real-time cryptocurrency prices, processes them, and stores the cleaned data for analytics and dashboard use.

Features

Pulls live price data from a public crypto API

Cleans, formats, and validates incoming data

Loads processed data into a database (PostgreSQL / SQLite)

Supports scheduled runs using cron or Airflow

Modular structure for adding more coins or data points

Tech Stack

Python

Requests / HTTPX

Pandas

PostgreSQL / SQLite

Airflow or Cron (optional)

Workflow

Extract – Fetch price, market cap, volume, and timestamps

Transform – Convert to proper formats, remove nulls, align schema

Load – Insert into the database for long-term storage or dashboards

Folder Structure
crypto-price-etl/
│── extract/
│   └── fetch_prices.py
│── transform/
│   └── clean_data.py
│── load/
│   └── load_to_db.py
│── utils/
│── main.py
│── requirements.txt
│── README.md

Run the Project

Install packages:

pip install -r requirements.txt


Start the pipeline:

python main.py

Future Improvements

Add more exchanges and data sources

Integrate with Supabase or BigQuery

Add a live dashboard (Streamlit)
