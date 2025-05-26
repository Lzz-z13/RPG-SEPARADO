import time
import os
import platform


def clearScreen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def typewriter(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Nova linha ao final