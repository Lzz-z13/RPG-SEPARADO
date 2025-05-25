def caminhos():
    import time
    import random
    from historia.initHis import typewriter, clearScreen
    from historia.initHis import personagem
    from assets.data import dic_nomes, dic_espadas

    escolha = input("\n1. O caminho da força. \n2. O caminho da sabedoria.\n3. O caminho da coragem.\n\n>> ")
    if escolha == "1":
        clearScreen()
        typewriter("caminho da força...")
        time.sleep(2)
        typewriter("Você se depara com um monstro feroz.")
        time.sleep(2)
        typewriter("\033[31;1mG:\033[m Você deve lutar contra ele.")
        time.sleep(2)
        typewriter("Você se prepara para a batalha.")
        
