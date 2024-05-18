termo_1 = int(input('informe o primeiro termo da PA: '))
razao = int(input('Quala a razão da PA: '))
for c in range(1,11):# for c in range(termo_1,10,razao)
    pa = termo_1 + (c-1)*razao
    print(pa,end=" -> ")
print('ACABOU')