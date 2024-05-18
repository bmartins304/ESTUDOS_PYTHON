s = 0
p = 0
from time import sleep
for i in range(1,500):
    if i%2 != 0 and i%3 == 0:
        p += 1
        s = s + i
print(p,s)
sleep(0.2)