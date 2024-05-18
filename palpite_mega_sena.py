import random
from time import sleep

numeros_mega = list()
jogos = list()
c = count =  0

print(f'{'mega sena':=^20}')
quantidade=int(input('quantos jogos serao feitos? '))
while c<quantidade:
    count = 0
    while True:
        numero_sorte = random.randint(1,60)
        if numero_sorte not in numeros_mega:
            numeros_mega.append(numero_sorte)
            count+=1
        if count>=6:
            break       
    jogos.append(numeros_mega[:])
    numeros_mega.clear()
    c+=1
    jogos.sort()
print(f'-='*3,f'sorteando {quantidade} jogos',f'-='*3)
for p,x in enumerate(jogos):
    print(f'jogo {p+1}: {x}')
    sleep(1.5)


