num = (int(input('primeiro número: ')),int(input('segudo número: ')),int(input('terceiro número: '))
       ,int(input('quarto número: ')))

print(f'os números digitados foram {num}')
print(f'o número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'o número três esta na posição {num.index(3) + 1}o')
else:
    print(f'nessa tupla não tem o número 3')

print('numeros pares',end=" ")
for c in range(0,len(num)):
    if  num[c] % 2 == 0:
        par = num[c]
        print(par,end=" ")       

    
    
