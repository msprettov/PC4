#PC4 
#Mauro Pretto 
#Empleo de librerías 
#3)
import requests


url = "https://unsplash.com/es/fotos/9LkqymZFLrE"

response = requests.get(url)

with open('perro.jpg', "wb") as f:
    f.write(response.content)
    

