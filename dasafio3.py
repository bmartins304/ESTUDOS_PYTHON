#media
nome = str(input('qual o nome do aluno? '))
n1 = float(input('informe a primeira nota: '))
n2 = float(input('informe a segunda nota: '))
m = (n1 + n2) / 2
print('o aluno > {} tem na primeria nota > {} e na segunda > {}, com a media de > {:.1f}'.format(nome,n1,n2,m))