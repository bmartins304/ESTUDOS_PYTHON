estado = dict()
brasil = list()
for x in range(0,3):
    estado['UF']= str(input('Qual a unidade Federativa: '))
    estado['sigla'] = str(input('Qual a sigla: '))
    brasil.append(estado.copy())
for e in brasil:
    for k in e.values():
        print(k)