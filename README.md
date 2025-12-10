



# **Crypto Price ETL**

Tracks crypto prices through a lightweight ETL pipeline. It pulls live market data, cleans it, and stores it for analysis or dashboards.

---

## **What This Project Does**

* Fetches live prices from a crypto API
* Cleans and validates the response
* Loads everything into a database
* Can run on a schedule (cron/Airflow)

---

## How It Works**

Extract → Transform → Load

* **Extract:** Get price, volume, market cap, timestamps
* **Transform:** Standardize fields, drop invalid rows
* **Load:** Save to PostgreSQL/SQLite

---

## **Tech Used**

* Python
* Pandas
* Requests/HTTPX
* PostgreSQL or SQLite
* Airflow/Cron (optional)

---

## **Structure**

```
crypto-price-etl/
  extract/
  transform/
  load/
  utils/
  main.py
  requirements.txt
```

---

## **Run It**

Install dependencies:

```
pip install -r requirements.txt
```

Start ETL:

```
python main.py
```



