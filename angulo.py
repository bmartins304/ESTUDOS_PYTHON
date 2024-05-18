import math

an = float(input('informe o ângulo em graus: '))
rad = math.radians(an)
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)
print('o seno, cosseno e tangente do ângulo {} e : {:.2f},{:.2f},{:.2f}'.format(an,seno,cosseno,tangente))