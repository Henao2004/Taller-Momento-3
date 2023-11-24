from analysis.analisisUsuarios import *
from analysis.analisisRefrigerio import *
from analysis.analisisSiembras import *
from helpers.crearPDF import convertir_csv_a_pdf
import os

if __name__ == "__main__":
    carpeta = "data"
    carpeta1 = "pdf"
    nombre_csv1 = "bdUsuarios.csv"
    nombre_csv2 = "bdSiembras.csv"
    nombre_csv3 = "bdRefrigerios.csv"
    nombre_pdf1 = "usuarios.pdf"
    nombre_pdf2 = "siembras.pdf"
    nombre_pdf3 = "refrigerios.pdf"
    ruta_csv1 = os.path.join(carpeta, nombre_csv1)
    ruta_csv2 = os.path.join(carpeta, nombre_csv2)
    ruta_csv3 = os.path.join(carpeta, nombre_csv3)
    ruta_pdf1 = os.path.join(carpeta1, nombre_pdf1)
    ruta_pdf2 = os.path.join(carpeta1, nombre_pdf2)
    ruta_pdf3 = os.path.join(carpeta1, nombre_pdf3)

    convertir_csv_a_pdf(ruta_csv1, ruta_pdf1)
    convertir_csv_a_pdf(ruta_csv2, ruta_pdf2)
    convertir_csv_a_pdf(ruta_csv3, ruta_pdf3)


