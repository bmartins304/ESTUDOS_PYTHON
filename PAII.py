primeiro_termo = int(input('informe o primeiro termo da PA: '))
razao = int(input('informe a razão da PA: '))
t = 1
while t < 11 :
    pa = primeiro_termo+(t - 1)*razao
    print(pa)
    t+=1
