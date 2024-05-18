
print('{:=^40}'.format(' LOJAS GUANABARA '))
valor_produto = float(input('Qual o valor do produto: '))
forma_pagamento = int(input('Qual será a forma de pagemento:\n'
                            '[1] à vista em dinheiro ou cheque (10 porcento de desconto)\n'
                            '[2] à vista no cartão (5 porcento de desconto)\n'
                            '[3] em ate 2X no cartão (Sem juros)\n'
                            '[4] Em até 3X a 10X no cartão (com juros de 20 porcento) \n'
                            ))
if forma_pagamento == 1:
    valor_pago = valor_produto -                                                                                                                                                                                                                                                                                                                                                                                ((valor_produto * 10) / 100) 
    print('Com a forma de pagamento à vista, o produto de R$ {} ficará por R$ {}.'.format(valor_produto,valor_pago))
elif forma_pagamento == 2 :
    valor_pago = valor_produto - ((valor_produto * 5) / 100) 
    print('Com a forma de pagamento à vista no cartão, o produto de R$ {} ficará por R$ {}.'.format(valor_produto,valor_pago))
elif forma_pagamento == 3:
    valor_pago = valor_produto / 2
    print('Em 2X no cartão, as parcelas do produto de valor R$ {} ficarão de R$ {} por mês.'.format(valor_produto,valor_pago))
elif forma_pagamento == 4:
    quant_parcelas=int(input('informe a quantidade de parcelas que irá pagar pelo produto: '))
    valor_pago = ((valor_produto * 20)  / 100) + valor_produto
    print('em {}X no cartão, as parcelas do produto de valor R$ {} ficarão de R$ {} por mês'.format(quant_parcelas,valor_produto,valor_pago))
else:
    print('Opção invalida!!')

