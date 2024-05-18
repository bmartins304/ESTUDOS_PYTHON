s= q= 0
while True:
    num = int(input('digite um número: '))
    if num == 999:
        break
    s+=num
    q+= 1
print(f'a quantidade de números digitados foram: {q}\nA soma dos números digitados foi: {s}')