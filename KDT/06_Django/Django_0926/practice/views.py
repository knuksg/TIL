from urllib import response
from django.shortcuts import render

# Create your views here.
def is_odd_even(request, number):
    odd_even = "홀수"
    if number == 0:
        odd_even = "0"
    elif number % 2 == 0:
        odd_even = "짝수"
    context = {"number": number, "odd_even": odd_even}
    return render(request, "practice/is-odd-even.html", context)


def calculate(request, number1, number2):
    calculate1 = number1 + number2
    calculate2 = number1 - number2
    calculate3 = number1 * number2
    calculate4 = number1 // number2
    context = {
        "number1": number1,
        "number2": number2,
        "calculate1": calculate1,
        "calculate2": calculate2,
        "calculate3": calculate3,
        "calculate4": calculate4,
    }
    return render(request, "practice/calculate.html", context)


def random_game(request):
    context = {}

    return render(request, "practice/random-game.html", context)


import random
import requests
import json


def result(request):
    pokemon = [
        {
            "name": "Bulbasaur",
            "img": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/001.png",
        },
        {
            "name": "Charmander",
            "img": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/004.png",
        },
        {
            "name": "Squirtle",
            "img": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/007.png",
        },
        {
            "name": "Pikachu",
            "img": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/025.png",
        },
        {
            "name": "Jigglypuff",
            "img": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/039.png",
        },
        {
            "name": "Meowth",
            "img": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/052.png",
        },
    ]
    random_number = random.choice(range(1, 20))
    api_pokemon = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{random_number}.png"
    url = "https://pokeapi.co/api/v2/pokemon/"
    response = requests.get(url)
    contents = response.text
    json_ob = json.loads(contents)
    api_pokemon_name = json_ob["results"][random_number]["name"]
    context = {
        "name": request.GET.get("name"),
        "pokemon": random.choice(pokemon),
        "api_pokemon": api_pokemon,
        "api_pokemon_name": api_pokemon_name,
    }
    return render(request, "practice/result.html", context)


def lipsum(request):
    context = {}
    return render(request, "practice/lipsum.html", context)


def lipsum_result(request):
    paragraph = request.GET.get("paragraph")
    word = request.GET.get("word")
    word_list = [
        "바나나",
        "짜장면",
        "사과",
        "포도",
        "딸기",
    ]
    lipsum_paragraph = []
    for i in range(int(paragraph)):
        lipsum_word = []
        for j in range(int(word)):
            lipsum_word.append(random.choice(word_list))
        lipsum_paragraph.append(lipsum_word)
    context = {
        "paragraph": paragraph,
        "word": word,
        "lipsum_paragraph": lipsum_paragraph,
    }
    return render(request, "practice/lipsum-result.html", context)


def index(request):

    return render(request, "practice/index.html")
