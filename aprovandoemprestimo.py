valor_casa = float(input('qual o valor da casa? '))
salario = float(input('informe o seu salário? '))
quantos_anos = float(input('Em quantos anos pretende pagar? '))

#As prestações > validação_salario

prestacoes = valor_casa/(quantos_anos * 12)
validacao_salario = (salario * 30) /100

if validacao_salario < prestacoes:
    print('Emprestimo nao aprovado!!!\n limite de 30 por cento do salário excedido!!\n Valor das prestações: {:.2f}\n valor dos 30 porcento do salário: {:.2f} '.format(prestacoes,validacao_salario))
elif validacao_salario > prestacoes:
    print('Tudo certo!! Você pagará R$ {:.2f} em {}anos'.format(prestacoes,quantos_anos))
 