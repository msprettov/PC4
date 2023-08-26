#PC4 
#Mauro Pretto 
# Base Datos  
#6)
import requests
import sqlite3

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()

conn = sqlite3.connect("cryptos.db")
c = conn.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS bitcoin (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        currency TEXT,
        price REAL,
        date TEXT
    )
""")

for currency, info in data["bpi"].items():
    c.execute("""
        INSERT INTO bitcoin (currency, price, date)
        VALUES (?, ?, ?)
    """, (currency, info["rate_float"], data["time"]["updated"]))

conn.commit()
conn.close()