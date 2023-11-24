from data.ListarSiembras import siembras
from helpers.crearCSV import crearCVSSiembras
from helpers.crearhtml import crearTabla

import pandas as pd

siembrasCSV = 'bdSiembras.csv'
siembrasPDF = 'siembras'

#Creamos la funcion crearCSVUsuarios
crearCVSSiembras(siembras,'bdSiembras.csv')

#Creando un dataframe desde una fuente csv
dataFrameSiembras=pd.read_csv('data/bdSiembras.csv')

#Convertir el DF en TABLA HTML
crearTabla(dataFrameSiembras,'siembras')

#Municipios mayores a 90 arboles
filtroUno=dataFrameSiembras.query("Cantidad>90")

#Municipio con Ceibas
filtroDos=dataFrameSiembras.query("Arbol=='Ceiba'")

#Municipio Siembras menor a 10
filtroTres=dataFrameSiembras.query("Cantidad<10")
