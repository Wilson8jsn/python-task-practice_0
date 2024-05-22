"""
age = 22

def check_age (*,age int);


if age > 18 :
    print ("you are an adult")
"""

"""
nombre = "Wilson"
lenguaje_favorito = "Python"

print(f"Hola, soy {nombre}. Estoy aprendiendo {lenguaje_favorito}.")

"""

"""
age = 22

def check_age(*, age: int):
    if age > 18:
        print("You are an adult")

check_age(age=age)

"""
def leer_colaboradores(filename):
    with open(filename, 'r') as file:
        colaboradores = file.read().splitlines()
    return colaboradores

def mostrar_colaboradores(colaboradores, n=5):
    for i, colaborador in enumerate(colaboradores[:n]):
        print(f"{i+1}. {colaborador}")

def agregar_colaborador(filename, nuevo_colaborador):
    colaboradores = leer_colaboradores(filename)
    if len(colaboradores) >= 15:
        print("No se puede agregar más colaboradores, el límite es 15.")
        return
    
    if nuevo_colaborador in colaboradores:
        print("El colaborador ya está en la lista.")
        return
    
    colaboradores.append(nuevo_colaborador)
    with open(filename, 'a') as file:
        file.write(f"\n{nuevo_colaborador}")
    print(f"Colaborador {nuevo_colaborador} agregado exitosamente.")

def main():
    filename = 'name.txt'
    
    while True:
        print("\n1. Mostrar colaboradores")
        print("2. Agregar colaborador")
        print("3. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            n = input("¿Cuántos colaboradores quieres mostrar? (por defecto 5): ")
            n = int(n) if n.isdigit() else 5
            colaboradores = leer_colaboradores(filename)
            mostrar_colaboradores(colaboradores, n)
        
        elif opcion == '2':
            nuevo_colaborador = input("Introduce el nombre del nuevo colaborador: ").strip()
            if nuevo_colaborador:
                agregar_colaborador(filename, nuevo_colaborador)
            else:
                print("Nombre inválido.")
        
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()