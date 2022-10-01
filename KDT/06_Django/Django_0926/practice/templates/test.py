import random
import requests
import json

url = "https://pokeapi.co/api/v2/pokemon/"
response = requests.get(url)
contents = response.text
json_ob = json.loads(contents)
api_pokemon_name = json_ob["results"][random.choice(range(19))]["name"]

print(api_pokemon_name, type(api_pokemon_name))
