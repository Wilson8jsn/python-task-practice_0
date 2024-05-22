# Importando el módulo
import calculator 

print(calculator.suma(4, 3))  # 7
print(calculator.resta(10, 9))  # 1


# Importando ciertas funciones
from calculator import suma, resta 
print(suma(4, 3))  # 7
print(resta(10, 9))  # 1