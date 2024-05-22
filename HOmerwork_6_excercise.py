# 1.- Hola Mundo: escribir un programa que imprima "Hola Mundo" en la terminal/consola.

print("Hola mundo")

# 2.- Calculadora: escribir un programa que tome dos números como entrada y realice operaciones básicas como suma, resta y multiplicación y división.

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

print(suma(6, 6))
print(resta(20, 10))

# 3.- Contador de palabras: escribe un programa que cuente el número de palabras en una cadena de texto dada.

with open('name.txt', 'r') as file:
    content = file.read()
    words = content.split()
    word_count = len(words)
    print("El numero es :", word_count)


# 4.- Adivina el número: escribe un programa que genere un número aleatorio y que permita al usuario adivinar cuál es.
# Proporcionar pistas como "Demasiado alto" y "Demasiado bajo" hasta que el usuario adivineel número.

import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 0
    
    print("¡Bienvenido a Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 20. ¿Puedes adivinar cuál es?")
    
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


# 5.- Listado de tareas: escribe un programa que permita al agregar, eliminar, y mostrar una lista de tareas pendientes.

def mostrar_menu():
    print("\nMenú de Tareas")
    print("1. Agregar Tarea")
    print("2. Eliminar Tarea")
    print("3. Mostrar Tareas")
    print("4. Salir")

def agregar_tarea(tareas):
    tarea = input("Escribe la nueva tarea: ")
    tareas.append(tarea)
    print("Tarea agregada.")

def eliminar_tarea(tareas):
    try:
        indice = int(input("Escribe el número de la tarea a eliminar: ")) - 1
        if 0 <= indice < len(tareas):
            tarea_eliminada = tareas.pop(indice)
            print(f"Tarea '{tarea_eliminada}' eliminada.")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Por favor, introduce un número válido.")

def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        print("\nListado de Tareas:")
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")

def main():
    tareas = []
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            agregar_tarea(tareas)
        elif opcion == '2':
            eliminar_tarea(tareas)
        elif opcion == '3':
            mostrar_tareas(tareas)
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor elige una opción del 1 al 4.")

if __name__ == "__main__":
    main()



#6.- Generador de contraseñas: escribe un programa que ga contraseña aleatoria de una longitud especificada por el usuario

import random
import string

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña

def main():
    while True:
        try:
            longitud = int(input("Introduce la longitud de la contraseña: "))
            if longitud < 1:
                print("La longitud debe ser un número positivo.")
            else:
                contraseña = generar_contraseña(longitud)
                print(f"Contraseña generada: {contraseña}")
                break
        except ValueError:
            print("Por favor, introduce un número válido.")

if __name__ == "__main__":
    main()