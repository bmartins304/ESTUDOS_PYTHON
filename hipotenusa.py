import math
co = float(input('informe o cateto oposto do triangulo: '))
ca = float(input('informe o cateto adjacente do triangulo: '))
h = math.sqrt((math.pow(co,2)) + (math.pow(ca,2)))
print('a soma dos catetos {}^2 + {}^2 = {:.3f}'.format(co,ca,h))