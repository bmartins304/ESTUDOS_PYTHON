def dobra(lst):
    pos=0
    while pos < len(lst):
        lst[pos] *= 2
        pos+=1
def soma(*valores):
    s=0
    for num in valores:
        s+=num
    print(f'os {valores} tem a soma de {s}')
valores = [4,5,2,7,9]
dobra(valores)
print(valores)
soma(4,3)
soma(1,3)