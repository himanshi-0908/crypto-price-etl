import requests
import pandas as pd
from datetime import datetime
import sqlite3
from db import init_db

def run_etl():
    # Initialize DB and get connection
    conn = init_db()
    
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd&include_24hr_change=true'
    
    try:
        res = requests.get(url).json()
    except Exception as e:
        print(f"Failed to fetch data from API: {e}")
        conn.close()
        return

    rows = []
    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    for c in res:
        try:
            name = c
            price = round(res[c]['usd'], 2)
            change = round(res[c]['usd_24h_change'], 2)
            rows.append([name, price, change, ts])
        except KeyError:
            print(f"Missing data for {c}, skipping...")
            continue

    if not rows:
        print("No data to insert. Exiting ETL.")
        conn.close()
        return

    df = pd.DataFrame(rows, columns=['name', 'price', 'change', 'timestamp'])

    # Insert data into DB safely
    with conn:
        df.to_sql('prices', conn, if_exists='append', index=False)

    conn.close()
    print('ETL run complete! Data loaded into crypto.db')

if __name__ == "__main__":
    run_etl()
