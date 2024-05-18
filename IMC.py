from math import pow

altura = float(input('informe a sua altura: '))
peso = float(input('informe o seu peso: '))

imc = peso /pow(altura,2)

if imc < 18.5:
    print(' o seu calculo do seu IMC deu: ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('o calculo do seu IMC deu: PESO IDEAL')
elif 25 <= imc < 30:
    print('o calculo do seu IMC deu: SOBREPESO')
elif 30 <= imc < 40:
    print('o calculo do seu IMC deu: OBESIDADE')
else:
    print('o calculo do seu IMC deu: OBESIDADE MORBIDA') 
    
print('{:.2f}'.format(imc))   