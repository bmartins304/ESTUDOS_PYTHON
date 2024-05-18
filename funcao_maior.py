from time import sleep
def maior(num):
    s=0
    for x in num:
        print(f'{x}',end=' ', flush=True)
        sleep(1)      
    print(f'foram informado {len(num)} numeros ao todo')
    for x in num:
        if x > s:
            s = x
    print(f'o maior valor é {s}')



a=[0,9,8]
b=[10,2,5,4]
c=[0,2,7,1]
maior(a)
maior(b)
maior(c)