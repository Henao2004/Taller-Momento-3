from data.ListaUsuarios import usuarios
from helpers.crearCSV import crearCVSUsuarios 
from helpers.crearhtml import crearTabla


import pandas as pd

usuariosCSV = 'bdUsuarios.csv'
usuariosPDF = 'usuarios'

#Creamos la funcion crearCSVUsuarios
crearCVSUsuarios(usuarios,'bdUsuarios.csv')

#Creando un dataframe desde una fuente csv
dataFrameUsuarios=pd.read_csv('data/bdUsuarios.csv')

#Convertir el DF en TABLA HTML
crearTabla(dataFrameUsuarios,'usuarios')

#Se filtran los datos
#filtroUno=dataFrameUsuarios.query("(Edad<30) and (Nombre=='Juan')")

#Encontrar los sembradores Mujeres mayores de 40 años y que ganen entre 1 y 2 SMMLV
filtroDos=dataFrameUsuarios.query("(Genero=='Mujer') and (Edad>40) and (Salario<=2320000)")

#Encontrar sembradores menores de 20 años
filtroTres=dataFrameUsuarios.query("Edad<20")

#Solo sembradores hombres mayores de 50
filtroCuatro=dataFrameUsuarios.query("(Genero=='Hombre' and (Edad>50))")