#API
#https://api.chucknorris.io/jokes/random
#https://rickandmortyapi.com/api/character
#https://api.chucknorris.io/jokes/random

"""
import requests

url = 'https://pokeapi.co/api/v2/pokemon/pikachu'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Error: {response.status_code}')
    
"""

import requests

url = "https://pokeapi.co/api/v2/pokemon/pikachu"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    abilities = [ability['ability']['name'] for ability in data['abilities']]
    print("Habilidades de Pikachu:")
    for ability in abilities:
        print(ability)
    
    
    with open("pikachu_abilities.txt", "w") as file:
        file.write("Habilidades de Pikachu:\n")
        for ability in abilities:
            file.write(ability + "\n")
else:
    print(f'Error: {response.status_code}')
