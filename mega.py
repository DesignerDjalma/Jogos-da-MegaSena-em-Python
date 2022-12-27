import os
import random
import platform
import time

def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'


def addCor(frase, cor: bcolors):
    return f"{cor}{frase}{bcolors.ENDC}"


def limpaTela() -> None:
    os.system('clear') if platform.system() == "Linux" else os.system('cls')


def jogos():
    numeros = [random.randint(1,60) for i in range(6)]
    numeros.sort()
    print(f"\nNúmeros:", addCor(f"{numeros}"[1:-1], bcolors.OKGREEN) ,"\n\n", sep='   ')
    return numeros


def bilhete(marcados: list):
    for i in range(1,61):    
        numero = f"{i:<3}"
        if i in marcados:
            numero = addCor(numero, bcolors.BOLD)
        else:
            numero = addCor(numero, bcolors.FAIL)
        if i % 10 == 0:
            print(numero,end='\n')
        else:
            print(numero,end=' ')


if __name__ == "__main__":
    for i in range(10):
        limpaTela()
        bilhete(jogos())
        time.sleep(0.2)
    print()


# print_format_table()
