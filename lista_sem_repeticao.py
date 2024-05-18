lista= list()
for num in range(0,5):
    valor = int(input('digite um valor: '))
    if num == 0 or valor > lista[-1]:
        lista.append(valor)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos,valor)
                break
            pos+=1    
print('*'*40)  
print(lista)