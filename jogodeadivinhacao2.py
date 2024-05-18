import random
tentativas = 0
numero_pc = random.randint(0,10)
numero_jogador = int(input('pense em um numero de 0 a 10: '))
if numero_jogador != numero_pc:
    print('você errou, tente novamente.')
    tentativas += 1
    while numero_pc != numero_jogador:
        numero_jogador = int(input('pense em um numero de 0 a 10: '))       
        if numero_pc != numero_jogador:
            print('você errou, tente novamente.')
            tentativas += 1
    print('em {} tentativas, você finalmente acertou o número que era {}'.format(tentativas,numero_pc))

    
    