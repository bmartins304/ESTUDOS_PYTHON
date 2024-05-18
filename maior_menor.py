import random

num = (random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10))
print('-__-'*50)
print(num)
print('-__-'*50)
ordem = sorted(num)
print(f'o menor valor é {ordem[0]}\nE o maior é {ordem[4]}')