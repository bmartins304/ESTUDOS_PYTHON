mais_velho = 0
total_idade = 0
mais_velho_idade =  0

woman = 0
total_idade_woman = 0

man = 0
total_idade_man  = 0
nome_mais_velho = ''

quat_idade = 0
print('='*50)
print('ANALISANDO CADASTROS')
print('='*50)
for c in range(1,5) : 
    nome = str(input('NOME: ')).strip().upper()
    genero = int(input('|informe o seu gênero:|\n|[1] MASCULINO|\n|[2] FEMININO|\n'))
    idade = int(input('informe a sua idade: '))

    total_idade += idade
    if genero == 1:
        man += 1
        total_idade_man += idade
        if idade > mais_velho:
            mais_velho = idade
            nome_mais_velho = nome
            mais_velho_idade = idade
            
    elif genero == 2:
        woman + 1
        total_idade_woman += idade
        if idade < 20 :
            quat_idade += 1
        
    
media_idade = total_idade/4
print('-'*50)
print('medias das idades é : {:.1f}'.format(media_idade))
print('o homem mais velho é o {} ,com {} anos de idade'.format(nome_mais_velho,mais_velho_idade))
print('a quantidade de mulheres abaixo de 20 anos de idade é : {}'.format(quat_idade))

    
