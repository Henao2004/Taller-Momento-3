import os
import pandas as pd
from tabulate import tabulate
from fpdf import FPDF

def convertir_csv_a_pdf(ruta_csv, nombre_pdf):
    # Verificar si la ruta del archivo es relativa o absoluta
    if not os.path.isabs(ruta_csv):
        # Si es relativa, convertir a absoluta
        ruta_csv = os.path.abspath(os.path.join(os.getcwd(), ruta_csv))

    # Extraer el nombre del archivo sin la extensión y la carpeta
    nombre_archivo, _ = os.path.splitext(os.path.basename(ruta_csv))

    # Cargar el archivo CSV
    datos = pd.read_csv(ruta_csv)

    # Convertir DataFrame a tabla
    tabla = tabulate(datos, headers='keys', tablefmt='grid')

    # Crear un objeto PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Agregar título al PDF
    pdf.cell(200, 10, txt=f"Datos de {nombre_archivo}", ln=True, align='C')

    # Agregar la tabla al PDF
    pdf.multi_cell(0, 10, txt=tabla)

    # Guardar el PDF
    pdf.output(nombre_pdf)

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