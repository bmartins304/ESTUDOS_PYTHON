import random
tentativas = 0
resposta = 'S'
while resposta == 'S':   
    numero_pc = random.randint(0,10)
    numero_jogador = int(input('Qual o número que o pc "pensou" de 0 a 10? '))
    if numero_pc != numero_jogador:
        print('você errou,tente novamente!!!')
        tentativas += 1
    else:
        print('em {} tentativas, você acertou o número do pc que era {}'.format(tentativas,numero_pc))
        print('-'*50)
        resposta = str(input('gostaria de tentar novamente? [s]/[n]')).upper()
print('jogo interrompido!!!')

    
    