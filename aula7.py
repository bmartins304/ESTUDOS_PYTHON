#nome = input('Qual o seu nome? ')
#print('prazer em te conhecer {:-^20}!'.format(nome))

n1 = int(input('digite um numero: '))
n2 = int(input('segundo numero: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
dI = n1 // n2
r = n1 % n2
e = n1 ** n2
print('a soma é {} ,\n a miltiplicação vale {} ,\n a divisao vale {:.3f}'.format(s,m,d), end=' > ')
print('a divisao inteira vale {} , o resto divisao é {}'.format(dI,r))
print('a exponeciação é {}'.format(e))