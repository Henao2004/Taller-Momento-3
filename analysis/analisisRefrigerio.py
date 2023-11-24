from data.ListaRefrigerios import refrigerio
from helpers.crearCSV import crearCVSRefrigerio
from helpers.crearhtml import crearTabla

import pandas as pd 

refrigerioCSV = 'bdRefrigerios.csv'
refrigerioPDF = 'refrigerio'

#Creamos la funcion crearCSVUsuarios
crearCVSRefrigerio(refrigerio,'bdRefrigerios.csv')

#Creando un dataframe desde una fuente csv
dataFrameRefrigerios=pd.read_csv('data/bdRefrigerios.csv')

#Convertir el DF en TABLA HTML
crearTabla(dataFrameRefrigerios,'refrigerios')

#Refrigerios costo unitario mayor 20.000
filtroUno=dataFrameRefrigerios.query("Precio>20000")

#Refrigerios costo total menor a 1000000
filtroDos=dataFrameRefrigerios.query("Costototal>1")

#Refrigerios que la cantidad sea menor a 1000
filtroTres=dataFrameRefrigerios.query("Cantidad<1000")
