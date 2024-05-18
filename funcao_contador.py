from time import sleep
def contador(i,f,p):

    if p < 0:
        p*= -1
    if p == 0:
        p = 1
        
    print(f'Contador de {i} até {f} em {p}')
   
    if i <f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont+=p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True) 
            sleep(0.5)
            cont -=p
        print('FIM')

contador(1,10,1)
contador(10,0,2)
print('agora é sua vez de personalizar a contagem!')
inicio = int(input('INICIO: '))
fim = int(input('FIM: '))
passo = int(input('PASSO: '))
contador(inicio,fim,passo)