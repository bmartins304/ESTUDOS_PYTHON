import random

n1 = str(input('nome do aluno: '))
n2 = str(input('nome do aluno: '))
n3 = str(input('nome do aluno: '))
n4 = str(input('nome do aluno: '))
lista = [n1,n2,n3,n4]
escolha = random.choice(lista)
print('o aluno escolhido foi: {}'.format(escolha))
