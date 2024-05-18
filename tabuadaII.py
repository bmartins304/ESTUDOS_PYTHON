resultado = 1
num = int(input('informe a tabuada que quer visualizar: '))
print('|','-'*10,'|')
for multicador in range(1,11):
    resultado = multicador * num    
    print('|{:2} X {:2} = {:2}|'.format(num,multicador,resultado))
print('|','-'*10,'|')
    
