import random
numero = list()
def sortear(lista):
    for i in range(0,5):
        lista.append(random.randint(1,10))
sortear(numero)
print(numero)


def somapar(a):
    s=0
    for i in a:
        if i%2 == 0 :
            s += i
    print(s)
somapar(numero)