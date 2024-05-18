import random
from time import sleep
m = random.randint(0,5)
adivi = str(input('adivinhe o numero do pc de 0 a 5: '))
adi = int(adivi)
print('processando...')
sleep(2)
if adi == m:
    print('o seu numero foi: {} e do pc foi {} \nparabens!!! voce acertou!! '.format(adi,m))
else:
    print('o seu numero foi {} e o do pc foi {}\ninfelizmente voce nao acertou!!!'.format(adi,m))
