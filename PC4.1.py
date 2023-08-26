#PC4 
#Mauro Pretto 
#Empleo de librerías 
#1) 

import requests
portafolio = int(input("Ingrese el número de bitcoins invertidos: "))
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
try: 
    response = requests.get(url)
    print(response.text)
    response.json()
    datos =response.json() 
    p_dolar = datos["bpi"]["USD"]["rate_float"]

    print(f"El valor de su inversión en bitcoins es de ${p_dolar*portafolio:,.4f}") 

except requests.RequestException: 
    print("El API no contiene la información")

