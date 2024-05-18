from datetime import date
maior_idade = 0
menor_idade = 0
for c in range(1,8):
    ano_nascimento = int(input('ano do seu nascimento: '))
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    if idade >= 21:
        maior_idade += 1
        print(idade)
    else:
        menor_idade += 1
        print(idade)
print('Aquantidade de pessoas que atingiu a maior idade foram: {} pessoas \ne Aquantidade de pessoas que ainda não atingiram a maior idade foram: {} pessoas'.format(maior_idade,menor_idade))
