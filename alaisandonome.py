#o nome com todas as letras maiusculas.
#o nome com todas minúsculas.
#quantas letras ao todo.(sem considerar espaços)
#Quantas letras tem o primeiro nome.

nome = str(input('digite o seu nome completo. :')).strip()
print('analisando nome...')
nM = nome.upper()
nm = nome.lower()
tl = len(nome) - nome.count(' ')
lp = nome.split()
ti ='analise finalizada'
print('{:=^20}\n o seu nome em Maiusculo : {} \n o seu nome em Minúsculo : {} \n A quantidade de letras sem espaçamento: {} \n Quantidade de letras no primeiro nome: {}'.format(ti,nM,nm,tl,len(lp[0])))
