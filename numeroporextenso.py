num = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez'
       ,'onze','doze','treze','quartoze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    ler_num = int(input('informe um  número entre 0 a 20: '))
    if ler_num > 20 or ler_num < 0:
        print('digite novamente.',end=" ")
    else:
        break
print(f'você digitou o número {num[ler_num]}')
