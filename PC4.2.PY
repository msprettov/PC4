#PC4 
#Mauro Pretto 
#Empleo de librerías 
#2) 
!pip install pyfiglet
import pyfiglet
import random

font = input("Ingrese el nombre de la fuente a utilizar (o presione Enter para seleccionar una fuente aleatoria): ")
if font == "":
    font = random.choice(pyfiglet.FigletFont.getFonts())

text = input("Ingrese el texto que desea imprimir: ")

figlet = pyfiglet.Figlet(font=font)
print(figlet.renderText(text))