import random
import time
from assets.things import clearScreen, typewriter

def dado():
    clearScreen()
    resultado = random.randint(1, 6)
    for i in range(3):
        typewriter("Rolando o dado", end = "")
        time.sleep(0.5)
        typewriter(".")
    return resultado 