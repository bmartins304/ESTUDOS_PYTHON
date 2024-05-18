'''nome = str(input('digite o seu nome: '))
if nome == 'bruno':
    print('seu nome é muito belo')
print('bom dia,{}'.format(nome))'''

n1 = float(input('digite a  primeira nota: '))
n2 = float(input('digite a segunda nota: '))
m = (n1 + n2)/2
print('a sua media foi {}'.format(m))
if m >= 6 :
    print('parabens!!! voce nao esta reprovado')
else:
    print('infelizmente, voce passara um tempo estudando mais um pouco!!!')