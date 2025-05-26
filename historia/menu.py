import time
import random
from assets.data import dic_nomes
from assets.things import clearScreen, typewriter
from historia.initHis import historia
perso = ""

def start(mortes):
    purg = False
    while True:
        clearScreen()
        print("""\033[1;32m
                 ______________________________
                |                              |
                |          WRAITHBOND          |
                |    UMA ALMA INSATISFEITA     |
                |______________________________|
        \033[m""")
        typewriter("\033[1m1. Iniciar")
        typewriter("2. Instruções")
        typewriter("3. Morrer...")
        typewriter("4. Purgatório\033[m\n")

        choice = input(">> ")
        if not choice.isdigit():
            typewriter("Entrada inválida. Por favor, digite um número.")
            time.sleep(1.5)
            continue

        choice = int(choice)

        if choice == 1:
            clearScreen()
            print("\033[37;1mIniciando o jogo", end="", flush=True)
            for _ in range(3):
                print(".", end="", flush=True)
                time.sleep(1)
            print()
            historia(personagem=dic_nomes[random.choice(list(dic_nomes.keys()))])
            break

        elif choice == 2:
            clearScreen()
            typewriter("\033[40;1m                ===== INSTRUÇÕES =====                \033[m")
            typewriter("Você é um espírito perdido em um mundo desconhecido.")
            typewriter("Faça escolhas digitando o número correspondente à opção desejada.")
            typewriter("Algumas escolhas podem levar à morte, outras ao progresso.")
            typewriter("O número de mortes será contado ao longo do jogo.")
            typewriter("Você pode reencarnar em outra alma se morrer.")
            typewriter("Seu objetivo é encontrar seu caminho e descobrir quem realmente é.")
            typewriter("Você deve rolar um dado para determinar seu destino.\n                   \033[35;1;4mBOA SORTE!\033[m")
            input("\nPressione Enter para voltar ao menu.\n>> ")

        elif choice == 3:
            mortes += 1
            typewriter("\nVocê infelizmente aceitou o seu destino...")
            time.sleep(1)
            typewriter("A morte o abraça. . .")
            time.sleep(2)

            input("\nPressione Enter para reencarnar em outra pobre alma...\n>> ")
            clearScreen()
            for i in range(3):
                print("Reencarnando" + "." * (i + 1))
                time.sleep(1)
                clearScreen()
            typewriter("Reencarnação concluída!")
            time.sleep(1.5)
            typewriter("Você acorda em um lugar desconhecido. Você não se lembra de nada.")
            time.sleep(2)
            typewriter("Você sente que está no mesmo lugar, mas com outro corpo.")
            time.sleep(2)
            typewriter(f"\n\033[1;31mMortes até agora: {mortes}\033[m")
            time.sleep(2)

        elif choice == 4 and not purg:
            typewriter("Você não pode ir para o purgatório ainda. Talvez em outra vida...")
            time.sleep(2)
        else:
            typewriter("Opção inválida. Tente novamente.")
            time.sleep(1.5)

    return mortes