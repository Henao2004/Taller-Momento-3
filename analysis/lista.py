import random

import pandas as pd


municipios_antioquia = [
    "Medellín",
    "Bello",
    "Itagüí",
    "Envigado",
    "Sabaneta",
    "Rionegro",
    "La Ceja",
    "Marinilla",
    "Copacabana",
    "Girardota",
    "Caldas",
    "La Estrella",
    "Sabaneta",
    "Amagá",
    "Guarne",
    "San Jerónimo",
    "Santa Fe de Antioquia",
    "Puerto Berrío",
    "Sonsón",
    "Jericó",
    "Andes",
    "Jardín",
    "Urrao",
    "Caucasia",
    "Apartadó",
    "Turbo",
    "Ituango",
    "Yarumal",
    "Valdivia",
    "Remedios",
    "Dabeiba",
    "El Bagre",
    "Zaragoza",
    "Puerto Nare",
    "Tarazá",
    "Segovia",
    "Vegachí",
    "Santo Domingo",
    "Anorí",
    "Cisneros",
    "San Pedro de los Milagros",
    "Santa Rosa de Osos",
    "Yalí",
    "San Andrés de Cuerquía",
    "Gómez Plata",
    "Yolombó",
    "Angostura",
    "Belmira",
    "Donmatías",
    "Santa Bárbara",
    "Santo Domingo",
    "El Peñol",
    "Granada",
    "San Rafael",
    "Concepción",
    "San Vicente",
    "El Santuario",
    "Guatapé",
    "Alejandría",
    "La Unión",
    "Cocorná",
    "Guadalupe",
    "Nariño",
    "Rionegro",
    "San Carlos",
    "San Francisco",
    "Carmen de Viboral",
    "La Unión",
    "El Carmen de Viboral",
    "Abejorral",
    "La Unión",
    "Sonsón",
    "Argelia",
    "Sonsón",
    "Nariño",
    "Salgar",
    "Cáceres",
    "Caucasia",
    "El Bagre",
    "Nechí",
    "Zaragoza",
    "San Roque",
    "Yarumal",
    "Valdivia",
    "Yalí",
    "Campamento",
    "Briceño",
    "Cisneros",
    "Yarumal",
    "San Andrés de Cuerquía",
    "Toledo",
    "Donmatías",
    "Girardota",
    "Barbosa",
    "Bello",
    "Medellín",
    "Itagüí",
    "Sabaneta",
    "La Estrella",
    "Caldas",
    "La Pintada",
    "Jericó",
    "Támesis",
    "Andes",
    "Jardín",
    "Santa Fe de Antioquia",
    "San Jerónimo",
    "Liborina",
    "Uramita",
    "Dabeiba",
    "Murindó",
    "Mutatá",
    "Chigorodó",
    "Carepa",
    "Apartadó",
    "San Juan de Urabá",
    "Arboletes",
    "Necoclí",
    "San Pedro de Urabá",
    "Turbo",
    "Vigía del Fuerte"
]

arboles_antioquia = [
    "Guayacán",
    "Ceiba",
    "Roble",
    "Pino",
    "Laurel",
    "Cedro",
    "Guanábana",
    "Mango",
    "Palma de cera",
    "Almendro",
    "Nogal",
    "Guacharaco",
    "Caucho",
    "Yarumo",
    "Arrayán",
    "Bambú",
    "Jacarandá",
    "Ficus",
    "Cascarillo",
    "Arrayán",
    "Papayo",
    "Guava",
    "Algarrobo",
    "Castaño",
    "Eucalipto",
    "Papaya",
    "Chagualo",
    "Pardillo",
    "Páramo",
    "Higuerón",
    "Palo de agua",
    "Nance",
    "Cilantro de monte",
    "Palo blanco",
    "Aromo",
    "Tamarindo",
    "Cafeto",
    "Aguacate",
    "Granadillo",
    "Tilo",
    "Higuerilla",
    "Pital",
    "Candelillo",
    "Guamo",
    "Chingalé",
    "Chorisia",
    "Piñuela",
    "Tamarindo",
    "Cuerno de alce",
]



datos = []

for _ in range(2000):

    municipio = random.choice(municipios_antioquia)
    arbol = random.choice(arboles_antioquia)
    cantidad = random.randint(200, 5000)  
    datos.append(f"En {municipio} se encuentra el árbol ({arbol}) en una cantidad de {cantidad}")

cantidad_de_datos = len(datos)

# Profe los datos se guardaran en este archivo txt para ver todos los datos 
with open("datos_arboles.txt", "w") as archivo:
    for dato in datos:
        archivo.write(f"{dato}\n")

print(f"Se generaron un total de {cantidad_de_datos} datos. Los datos se han guardado en 'datos_arboles.txt'.")


#Creacion de dataframe con pandas utilizando esta lista 

df = pd.DataFrame(datos, columns=["Información"])

print(df.head())

# Profe los datos se guardaran en este archivo csv para ver todos los dataframe
df.to_csv("datos_arboles_dataframe.csv", index=False)


cantidad = random.randint(100,5000)



