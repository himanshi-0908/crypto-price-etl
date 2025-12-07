import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(page_title='Crypto Dashboard', layout='wide')

def load():
    conn = sqlite3.connect('crypto.db')
    df = pd.read_sql('SELECT * FROM prices ORDER BY id DESC LIMIT 30', conn)
    conn.close()
    return df

st.title('📊 Live Crypto Dashboard')

df = load()

if df.empty:
    st.warning('No data yet. Run etl.py.')
else:
    col1, col2, col3 = st.columns(3)
    coins = df['name'].unique()

    for i, coin in enumerate(coins):
        cd = df[df['name'] == coin].iloc[0]
        with [col1, col2, col3][i]:
            st.metric(label=coin.upper(), value=f"${cd['price']:.2f}", delta=f"{cd['change']:.2f}%")

    st.subheader('Trend Chart')
    chart = df.pivot(index='timestamp', columns='name', values='price')
    st.line_chart(chart)
