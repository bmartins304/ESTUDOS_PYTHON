import random

vol = random.randint(60,100)
if vol >= 80:
    multa =abs( (80 - vol) * 7)
    print('ATENÇÃO!!! VOCE ESTA SENDO MULTADO POR EXECESSO DE VELOCIDADE. \n VELOCIDADE ATUAL: {} KM/H\n VELOCIDADE PERMITIDA: 80 KM/H\n VALOR DA MULTA: R$ {} REAIS'.format(vol,multa))
else:
    print('{} KM/H VELOCIDADE PERMITIDA'.format(vol))