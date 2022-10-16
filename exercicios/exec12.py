p = int(input('Preco do produto: R$'))

desc = 10
produto = p - (p * desc / 100)

print('o produto que custava {} reais, na promoção de {}% vai custar {:.2f} reais'.format(p, desc, produto))