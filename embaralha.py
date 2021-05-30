import random
import sys
import time


def embaralha(nome):
    conjunto = list(nome)
    conjuntoV  = set(conjunto)
    if len(conjunto) != len(conjuntoV):
        while len(conjunto) != len(conjuntoV):
            print(embaralha(str(input('Palavra: '))))
            if len(conjunto) == len(conjuntoV):
                break
    else:
        sair = int(input('SAIR[1/2]? '))
        if sair == 1:
            print('Finalizando...')
            time.sleep(3)
            sys.exit()

             
                
    repetidos = []
    letras = []
    limite = -1
    tentativas = 0
    x = list(nome)
    while True:
        tentativas += 1
        limite += 1
        aleatorio = random.choice(x)
        if limite == len(x):
            for x in letras:
                print(x, end="")
            print('')  
            return f'TENTATIVAS = {tentativas}'
         
        if aleatorio in repetidos:
            while True:
                tentativas += 1
                aleatorio = random.choice(x)
                if aleatorio not in repetidos:
                    letras.append(aleatorio)
                    repetidos.append(aleatorio)
                    break 
        else:
            repetidos.append(aleatorio)
            letras.append(aleatorio)


while True:
    print('Utilize apenas palavras sem letras repetidas!')
    time.sleep(2)
    print(embaralha(str(input('Palavra: '))))
   
    