n1 = float(input('informe a primeira nota do aluno: '))
n2 = float(input('informe a segunda nota do aluno: '))

media = (n1 + n2) /2

if media < 5:
    print('com a média de {:.1f} pontos, o aluno está \033[4;31mreprovado\033[m!!'.format(media))
elif media >= 5 and media <= 6.9:   # if (5<= media <= 6,9):
    print('com a média de {:.1f} pontos, o aluno está de \033[4;31mrecuperação\033[m!!'.format(media))
elif media >= 7:
    print('com a média de {:.1f} pontos, o aluno está \033[4;32maprovado\033[m!!'.format(media))