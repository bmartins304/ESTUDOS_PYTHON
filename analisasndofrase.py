frase = str(input('digite uma frase aqui: ')).strip()
print('analisando frase...')
A = frase.lower().count('a')
AI = frase.lower().find('a') + 1
AU = frase.lower().rfind('a') + 1
print('a quantidade de letras A: {}'.format(A))
print('a posiçao da primeira letra A: {}'.format(AI))
print('a ultima posição da letra A: {}'.format(AU))