via = int(input('qual a distancia da viagem? '))
if via <= 200:
    din = 0.5 * via
    print('a viagem de {} custará {}'.format(via,din))
elif via > 200:
    din = 0.45 * via
    print('a viagem de {} custará {}'.format(via,din))