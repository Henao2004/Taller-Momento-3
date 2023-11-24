import random

usuarios = []
nombres_y_generos = {
    'Juan': 'Hombre',
    'Andrea': 'Mujer',
    'Sara': 'Mujer',
    'Jorge': 'Hombre',
    'Tomas': 'Hombre',
    'Fabian': 'Hombre',
    'David': 'Hombre',
    'Alejo': 'Hombre',
    'Camila': 'Mujer',
    'Daniela': 'Mujer',
    'Laura': 'Mujer',
    'Valentina': 'Mujer',
    
}

for _ in range(50):
    nombre = random.choice(['Juan', 'Andrea', 'Sara', 'Jorge', 'Camila', 'Tomas', 'Daniela', 'Fabian', 'Laura', 'David', 'Valentina', 'Alejo'])
    contrasena = random.choice(['admin123', 'arboles000'])
    edad = random.randint(18, 62)
    salario = random.randint(1160000, 5000000)
    genero = nombres_y_generos[nombre]  # Obtiene el género del diccionario
    usuario = [nombre, contrasena, edad, salario, genero]  # Agregar el género a la lista del usuario
    usuarios.append(usuario)
