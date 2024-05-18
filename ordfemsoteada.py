from random import shuffle
n1 = str(input('nome do aluno: '))
n2 = str(input('nome do aluno: '))
n3 = str(input('nome do aluno: '))
n4 = str(input('nome do aluno: '))
lista = [n1,n2,n3,n4]
shuffle(lista)
print('a ordem embaralhada será:')
print(lista)