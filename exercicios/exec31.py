d = float(input('Distancia da viagem em KM: '))

preco1 = d * 0.50
preco2 = d * 0.45

if d <= 200:
    print('Sua viagem vai custar {:.2f} reais'.format(preco1))
else:
    print('Sua viagem vai custar {:.2f} reais'.format(preco2))