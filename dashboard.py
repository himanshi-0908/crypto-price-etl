import streamlit as st
import pandas as pd
import sqlite3
import requests
from datetime import datetime
from db import init_db

st.set_page_config(page_title='Crypto Dashboard', layout='wide')

# --- ETL Step: fetch live data and insert into DB ---
def run_etl():
    conn = init_db()
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd&include_24hr_change=true'
    
    try:
        res = requests.get(url).json()
    except Exception as e:
        st.error(f"Failed to fetch data from API: {e}")
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
            continue

    if rows:
        df = pd.DataFrame(rows, columns=['name', 'price', 'change', 'timestamp'])
        with conn:
            df.to_sql('prices', conn, if_exists='append', index=False)
    conn.close()

# --- Load data from DB ---
def load_data():
    try:
        conn = init_db()
        df = pd.read_sql('SELECT * FROM prices ORDER BY id DESC LIMIT 30', conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        return pd.DataFrame()

# Run ETL first
run_etl()

st.title('📊 Live Crypto Dashboard')

df = load_data()

if df.empty:
    st.warning('No data available.')
else:
    col1, col2, col3 = st.columns(3)
    coins = df['name'].unique()

    for i, coin in enumerate(coins):
        cd = df[df['name'] == coin].iloc[0]
        with [col1, col2, col3][i % 3]:
            st.metric(label=coin.upper(), value=f"${cd['price']:.2f}", delta=f"{cd['change']:.2f}%")

    st.subheader('Trend Chart')
    chart = df.pivot(index='timestamp', columns='name', values='price')
    st.line_chart(chart)
