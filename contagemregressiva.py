import emoji
from time import sleep
for c in range(10,0,-1):
    print('{}...'.format(c))
    sleep(1)
print('{}...explosões...{}'.format(emoji.emojize(':fireworks:'),emoji.emojize(':fireworks:')))