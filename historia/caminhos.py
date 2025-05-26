from caminhosv2.forca import forca
from assets.things import clearScreen, typewriter

def caminhos(personagem):
    from historia.initHis import personagem
    import time
    import random
    from historia.initHis import typewriter, clearScreen
    from assets.data import dic_nomes, dic_espadas

    escolha = input("\n1. O caminho da força. \n2. O caminho da sabedoria.\n3. O caminho da coragem.\n\n>> ")
    if escolha == "1":
        forca(personagem)