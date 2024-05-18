palavras = ('APRENDER','BORRACHA','LAGRIMAS','MICROFONE','ABELHA','CORNO','CHIFRE'
            ,'ZUMBIDO','CACHAÇA','MOMOCA','MOTOSSERRA')

for c in palavras:
    print(f'\nna palavra {c} temos',end=' ')
    for letras in c :
        if letras.upper() in 'AEIOU':
            print(letras,end=' ')


