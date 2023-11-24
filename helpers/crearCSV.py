import csv

def crearCVSUsuarios(lista,nombreArchivo):
   with open('data/'+nombreArchivo,mode='w',newline='',encoding='utf-8')as archivoCSV:
        writer=csv.writer(archivoCSV)
        writer.writerow(['Nombre','Contraseña','Edad','Salario','Genero'])
        writer.writerows(lista)
        
def crearCVSRefrigerio(lista,nombreArchivo):
    with open('data/'+nombreArchivo,mode='w',newline='',encoding='utf-8')as archivoCSV:
        writer=csv.writer(archivoCSV)
        writer.writerow(['Almuerzo','Precio','Cantidad','Costototal'])
        writer.writerows(lista)
        
def crearCVSSiembras(lista,nombreArchivo):
    with open('data/'+nombreArchivo,mode='w',newline='',encoding='utf-8')as archivoCSV:
        writer=csv.writer(archivoCSV)
        writer.writerow(['Municipio','Arbol','Cantidad'])
        writer.writerows(lista)


        
