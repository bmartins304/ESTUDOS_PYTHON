quilo = float(input('Qual a quilometragem pecorida? '))
dias = int(input('por quantos dias foi alugado? '))

Pd = 60 * dias

Pq = quilo * 0.15

total = Pd + Pq

print('em {} dias com {} KM peccorridos serao pagos terá um custo de R$ {} \n sendo R$ {} custo por dias e R$ {} custo por KM'.format(dias,quilo,total,Pd,Pq))