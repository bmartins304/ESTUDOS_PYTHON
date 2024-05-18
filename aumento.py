sala = float(input('Qual o valor do salario? '))
aumen = (sala * 15) / 100
salaN = sala + aumen
print('o salario de R$ {} reais, com o aumento ficará R$ {:.2f} reais'.format(sala,salaN))