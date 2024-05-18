times = ('palmeiras','gremio','atlerico mineiro MG', 'flamengo', 'botafogo','red bull bragantino','fluminense'
         ,'paranaense','internacional','fortaleza','sao paulo', 'cuiaba','corinthias','cruzeiro','vasco','bahia'
         ,'santos','goiás','coritiba','américa')
print('-='*50)
print(f'os 5 primeiros colocados sao {times[0:5]}')
print('='*40)
print(f'o ultimos 4 colocados da tabela são {times[-4:]}')
print('='*40)
print('em ordem alfabética ',sorted(times))
print('='*40)
print(f'posição do vasco = {times.index('vasco') + 1}o posição')