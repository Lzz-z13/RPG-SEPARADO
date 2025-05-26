import random
import time

dic_espadas = {
    "A" : "Canivete", "dano" : 3,
    "B" : "Espada Básica", "dano" : 5,
    "C" : "Long Sword", "dano" : 7,
}
dic_nomes = {
    "A" : {"nome" : "José", "vida" : 70, "dano" : +3,},
    "B" : {"nome" : "Maria", "vida" : 75, "dano" : +4,},
    "C" : {"nome" : "João", "vida" : 80, "dano" : +5,}
}

def nome_al():
    return random.choice(list(dic_nomes.keys()))