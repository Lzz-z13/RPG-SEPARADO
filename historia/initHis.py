import time
from historia.caminhos import caminhos
from assets.things import clearScreen
from assets.things import typewriter
from assets.data import dic_espadas
from assets.data import nome_al
personagem = nome_al()  # Sorteia personagem 1 vez

def historia(personagem):
    nome = personagem["nome"]
    vida = personagem["vida"]
    dano = personagem["dano"]

    typewriter("Você abre os olhos e decide se levantar.")
    time.sleep(2)
    typewriter("Você não se lembra de absolutamente nada.")
    time.sleep(2)
    typewriter("Mas você sente que sabe de algo...")
    typewriter(f"\033[31;1m???\033[m: Seu nome é {nome}")
    time.sleep(1)
    typewriter("\033[31;1m???\033[m: Você não deveria estar aqui.")
    time.sleep(1)
    typewriter("\033[31;1m???\033[m: Eu sou o seu guia a partir de agora.")
    time.sleep(1)
    typewriter("\033[31;1mG\033[m: Pode me chamar de G...")

    ja_perguntou_1 = False
    ja_perguntou_2 = False

    while True:
        typewriter("\n\033[1mO que você quer perguntar?\033[m")
        print("1. Onde estou?")
        time.sleep(1)
        print("2. O que você quer dizer com 'guia'?")
        time.sleep(1)
        print("3. Sair do diálogo")
        time.sleep(1)

        choice = input("\n>> ")

        if choice == "1" and not ja_perguntou_1:
            ja_perguntou_1 = True
            typewriter("\033[31;1mG:\033[m Você está em um lugar entre a vida e a morte.")
            time.sleep(2)
            typewriter("\033[1mComo assim?")
            time.sleep(1)
            typewriter("\033[31;1mG:\033[m Você está morto, mas ainda não está pronto para ir.")
            time.sleep(1)
            typewriter("\033[31;1mG:\033[m Você deve passar por um teste para decidir seu destino.")
            time.sleep(1)
        elif choice == "2" and not ja_perguntou_2:
            ja_perguntou_2 = True
            typewriter("\033[31;1mG:\033[m Eu sou o seu guia, vou te ajudar a passar pelo teste.")
            time.sleep(1)
            typewriter("\033[31;1mG:\033[m Você deve enfrentar um desafio para decidir seu destino.")
            time.sleep(1)
            typewriter("\033[31;1mG:\033[m Dentre esses 3 caminhos, você deve escolher um.")
            time.sleep(1)
            typewriter("\033[1m   1. O caminho da força.\n   2. O caminho da sabedoria.\n   3. O caminho da coragem.\033[m")
            time.sleep(3)
            typewriter("\033[31;1mG:\033[m O caminho da força é o mais fácil, mas o mais perigoso.")
            time.sleep(2)
            typewriter("\033[31;1mG:\033[m O caminho da sabedoria é o mais difícil, mas o mais seguro.")
            time.sleep(2)
            typewriter("\033[31;1mG:\033[m O caminho da coragem é o mais equilibrado.")
            time.sleep(1)
            input("\033[1mPressione Enter para continuar...\n>> ")
            clearScreen()

        elif choice == "3":
            typewriter("\033[31;1mG:\033[m Já que você está pronto, vou te dar um canivete.")
            time.sleep(2)
            typewriter(f"\033[31;1mG:\033[m Aqui está sua arma: {dic_espadas['A']}")
            time.sleep(1)
            typewriter("Você pega a espada e sente que ela é leve, mas fraca e sem poder.")
            time.sleep(1)
            typewriter("\033[31;1mG:\033[m Agora você está pronto para começar sua jornada.")
            time.sleep(1)
            input("\033[1mPressione Enter para continuar...\n>> ")
            clearScreen()
            break
        else:
            typewriter("Você já perguntou isso ou digitou algo inválido.")
            time.sleep(1.5)
    # Função para iniciar os caminhos
    caminhos(personagem)