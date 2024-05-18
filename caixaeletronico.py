nota_50   = 0
nota_20   = 0
nota_10   = 0
nota_1    = 0
count     = 0
sacamento = 0
validacao = 0

print('='*50)
print('CAIXA ELETRONIQUINHO')
print('='*50)

while True:
    dinheiro = int(input('quanto irá sacar: R$'))
    #acima de 50
    if dinheiro >= 50:
        nota_50 = dinheiro//50
        sacamento = 50 * nota_50
        validacao = dinheiro-sacamento
        if validacao != 0:
            nota_20 = validacao//20
            sacamento = 20 * nota_20
            validacao = validacao - sacamento
            if validacao != 0:
                nota_10 = validacao//10
                sacamento = 10 * nota_10
                validacao = validacao - sacamento
                if validacao != 0 :
                    nota_1 = validacao//1
                    sacamento = 1 * nota_1
                    validacao = validacao - sacamento
                else:
                    break
            else:
                break
        else:
            break
       # abaixo de 50 
    else:
        if  dinheiro < 50:
            nota_20 = dinheiro//20
            sacamento = 20 * nota_20
            validacao = dinheiro - sacamento
            if validacao != 0 :
                nota_10 = validacao//10
                sacamento = 10 * nota_10
                validacao = validacao - sacamento
                if validacao != 0:
                    nota_1 = validacao//1
                    sacamento = 1 * nota_1
                    validacao = validacao - sacamento
                else:
                    break
            else:
                break    
    break        

print('-'*50)
if nota_50 > 0 :
    print(f'será sacado {nota_50} notas de R$ 50.')
if nota_20 > 0:
    print(f'será sacado {nota_20} notas de R$ 20.')
if nota_10 > 0 :
    print(f'será sacad0 {nota_10} notas de R$ 10.')
if nota_1 > 0 :
    print(f'será sacado {nota_1} notas de R$ 1.')
print('-='*50)
print('Tenha um bom dia, volte sempre!')




   