n = s = 0
while True:
    n = int(input('digite um número: '))           
    if n == 999:
        break
    s+= n
print(f'a soma dos números digitados é igual a:  {s}')