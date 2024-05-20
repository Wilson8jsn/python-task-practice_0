
# Leer todo 
"""

with open('nombres.txt', 'r') as file:
    contenido = file.read()
    print(contenido)
    
"""    

 # Leer solo ciertas rangos   

"""

with open('nombres.txt', 'r') as file:
    contenido = file.read()
    print(contenido[0:6])
    
 """
    
 # Leer solo  una lineas  
 
"""
with open('nombres.txt', 'r') as file:
    contenido = file.readline()
    print(contenido) 
    
"""
    
 # Leer solo la segunda linea
"""
with open('nombres.txt', 'r') as file:
    contenido = file.readline()  
    contenido = file.readline() 
    print(contenido)
""" 
   
   
# Funcion  
    
def imprimir_lineas(num_lineas):
    with open('nombres.txt', 'r') as file:
        for _ in range(num_lineas):
            contenido = file.readline()
            print(contenido)
            
imprimir_lineas(2)
