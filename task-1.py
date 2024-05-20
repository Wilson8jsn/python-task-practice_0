# Crear hola mundo en la terminal 

print("Hola mundo")

# Suma y resta 

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

print(suma(6, 6))
print(resta(20, 10))

# Contador de palabras

with open('name.txt', 'r') as file:
    content = file.read()
    words = content.split()
    word_count = len(words)
    print("El numero es :", word_count)


# Adivina

import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    
    print("¡Bienvenido a Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?")
    
    while True:
        intento = int(input("Introduce tu suposición: "))
        intentos += 1
        
        if intento == numero_secreto:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break
        elif intento < numero_secreto:
            print("Demasiado bajo. ¡Intenta con un número más alto!")
        else:
            print("Demasiado alto. ¡Intenta con un número más bajo!")

adivina_el_numero()


