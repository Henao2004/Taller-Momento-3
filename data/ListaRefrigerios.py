import random
refrigerio=[]

for _ in range(50):
    almuerzo=random.choice(['Sandwich','Hamburguesa','Bandeja Paisa'])
    precio=random.randint(15000,20000)
    cantidad=random.randint(500,5000)
    costoTotal=(precio*cantidad)
    comida=[almuerzo,precio,cantidad,costoTotal]
    refrigerio.append(comida)
        