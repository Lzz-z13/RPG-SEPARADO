# forca.py

import time
from assets.things import typewriter, clearScreen
from assets.data import dic_nomes
from resources.dado import dado

def forca(personagem):  # personagem = "A", "B", ou "C"
    clearScreen()
    typewriter("Você escolheu o caminho da força...")
    time.sleep(2)
    nome = dic_nomes[personagem]['nome']
    vida_jogador = dic_nomes[personagem]['vida']
    dano_base  =dic_nomes[personagem]['dano']

    print(f"{nome} tem:\n{vida_jogador} de HP;\nCausa {dano_base} de dano.")
    time.sleep(4)
    clearScreen()
    typewriter("Caminho da força...")
    time.sleep(2)
    typewriter("Você se depara com um monstro feroz.")
    time.sleep(2)
    typewriter("\033[31;1mG:\033[m Você deve lutar contra ele.")
    time.sleep(2)
    typewriter("Você se prepara para a batalha.")
    time.sleep(2)

    # Dados do monstro
    vida_monstro = 35
    while vida_monstro > 0 and vida_jogador > 0:
        typewriter(f"{nome} ataca!")
        time.sleep(1)
        rolagem = dado()
        time.sleep(1)

        if rolagem <= 2:
            dano_causado = dano_base
            typewriter(f"Ataque fraco... Você causou apenas {dano_causado} de dano.")
        elif rolagem <= 4:
            dano_causado = dano_base + 2
            typewriter(f"Ataque bom! Você causou {dano_causado} de dano.")
        else:
            dano_causado = dano_base + 5
            typewriter(f"Ataque crítico! Você causou {dano_causado} de dano!")

        vida_monstro -= dano_causado
        time.sleep(2)

        if vida_monstro > 0:
            typewriter(f"O monstro ainda tem {vida_monstro} de vida.")
            time.sleep(1)
            typewriter("O monstro contra-ataca!")
            time.sleep(1)
            rolagem = dado()
            dano_monstro = rolagem + 2
            vida_jogador -= dano_monstro
            typewriter(f"Você sofreu {dano_monstro} de dano! Vida restante: {vida_jogador}")
        else:
            typewriter("Você derrotou o monstro!")

    if vida_jogador <= 0:
        typewriter("\n\033[31mVocê foi derrotado na batalha...\033[m")
    elif vida_monstro <= 0:
        typewriter("\n\033[32mVitória! O monstro foi vencido.\033[m")
    else:
        typewriter("\nA batalha terminou, mas o combate continua...")

    return