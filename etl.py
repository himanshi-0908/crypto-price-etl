import requests
import pandas as pd
from datetime import datetime
import sqlite3
from db import init_db

init_db()

url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd&include_24hr_change=true'
res = requests.get(url).json()

rows = []
ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

for c in res:
    rows.append([c, res[c]['usd'], res[c]['usd_24h_change'], ts])

df = pd.DataFrame(rows, columns=['name', 'price', 'change', 'timestamp'])

conn = sqlite3.connect('crypto.db')
df.to_sql('prices', conn, if_exists='append', index=False)
conn.close()

print('Loaded')
