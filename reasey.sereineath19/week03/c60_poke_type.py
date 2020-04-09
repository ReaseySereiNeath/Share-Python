import requests


def poke_type(pokemon):
    poker_list = []
    poker = requests.get\
        ("https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json").json()
    for i in poker["pokemon"]:
        if all(a in i["type"] for a in pokemon):
            poker_list.append((i["id"], i["name"]))
    return poker_list
