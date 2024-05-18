iqual = 0

frase = str(input('digite a frase aqui: ')).strip().upper()

sem_espaco = frase.split()
sem_espaco2 = ''.join(sem_espaco)

ult_termo = len(sem_espaco2) - 1

for i in range(0,len(sem_espaco2)):
    if sem_espaco2[i] == sem_espaco2[ult_termo - i]:
        iqual += 1

if iqual == len(sem_espaco2):
    print('essa frase é um polindromo!!')
else:
    print('essa frase não é um polindromo!!')


    '''print(frase[i])
    print(frase[ult_termo - i])'''

