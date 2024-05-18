import random
from time import sleep
soma = 0

quantas_vezes_ganhou = 0

print('-'*40)
print('jogo do impar ou par')
print('-'*40)

while True:

    num= int(input('escolha um número de 1 a 10: '))    
    par_ou_impar = str(input('você quer par ou impar: [P/[I]] ')).upper()

    num_pc = random.randint(1,10)
    soma = num_pc + num
    print('='*40)
    print(f'o jogador escolheu: {par_ou_impar} e o número foi : {num} \nnúmero do pc: {num_pc}\nA soma é: {soma}')
    sleep(2)
    if par_ou_impar == 'P':
        if soma % 2 == 0:
            print('='*40)
            print('\033[32mvocê ganhou!\033[m')
            print('jogue novamente...')
        else:
            print('='*40)
            print('\033[35mvocê perdeu!!!\033[m')
            break
    elif par_ou_impar == 'I':
        if soma % 2 != 0:
            print('='*40)
            print('\033[32mvocê ganhou!!\033[m')
            print('jogue novamente...')
        else:
            print('='*40)
            print('\033[35mvocê perdeu!!!\033[m')
            break

    quantas_vezes_ganhou += 1
print(f'você ganhou {quantas_vezes_ganhou} vezes')
