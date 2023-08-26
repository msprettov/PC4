#PC4 
#Mauro Pretto 
#Manejo de archivos 
#5)
import requests
import csv

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()

with open("bitcoin.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Currency", "Price", "Time"])
    for currency, info in data["bpi"].items():
        writer.writerow([currency, info["rate"], data["time"]["updated"]])

with open("bitcoin.txt", "w") as f:
    for currency, info in data["bpi"].items():
        f.write(f"{currency}: {info['rate']}\n")
        f.write(f"Time: {data['time']['updated']}\n")

  
     
