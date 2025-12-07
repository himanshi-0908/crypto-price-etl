import streamlit as st
import pandas as pd
import sqlite3
from db import init_db

st.set_page_config(page_title='Crypto Dashboard', layout='wide')

# Load data from database with error handling
def load():
    try:
        conn = init_db()  # get connection from db.py
        df = pd.read_sql('SELECT * FROM prices ORDER BY id DESC LIMIT 30', conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Failed to load data from database: {e}")
        return pd.DataFrame()  # return empty DataFrame if error

st.title('📊 Live Crypto Dashboard')

df = load()

if df.empty:
    st.warning('No data yet. Run etl.py or check your database.')
else:
    col1, col2, col3 = st.columns(3)
    coins = df['name'].unique()

    # Display metrics for each coin
    for i, coin in enumerate(coins):
        cd = df[df['name'] == coin].iloc[0]
        with [col1, col2, col3][i % 3]:  # ensure no index error
            st.metric(label=coin.upper(), value=f"${cd['price']:.2f}", delta=f"{cd['change']:.2f}%")

    # Trend chart
    st.subheader('Trend Chart')
    chart = df.pivot(index='timestamp', columns='name', values='price')
    st.line_chart(chart)
