t = 0
media = 0
maior = 0
menor = 0
while t < 5 :
    num = float(input('digite um número: '))
    media += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    t+=1
print(maior,menor,media)