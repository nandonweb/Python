v = int(input('Digite o valor do produto: R$'))
e = int(input('Digite uma opcao: '))

avista = v - (v * 10 / 100)
avista_cartao = v - (v * 5 / 100)
cartao3x = v + (v * 20 / 100)

if e == 1:
    print('a vista dinheiro/cheque: 10% de desconto R${:.2f}'.format(avista))
elif e == 2:
    print('avista no cartão: 5% de desconto {:.2f}'.format(avista_cartao))
elif e == 3:
    print('em até 2x no cartão preço normal {:.2f}'.format(v))
elif e == 4:
    print('3x ou mais no cartão: 20% de juros {:.2f}'.format(cartao3x))

