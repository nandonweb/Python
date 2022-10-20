s = int(input('Qual seu salario: '))
o = int(input('Qual seu objetivo, digite 1 para casa e 2 para 1 milhão '))

print('Seu salario é R${:.2f} por mes e acumulando em 1 ano sera R${:.2f}'.format(s, s*12))

casa = 250000
ummilhao = 1000000

if o == 1:
    print('Para comprar uma casa de {:.2f} reais voce precisa de {:.0f} meses ganhando {}'.format(casa, (casa/s), s))
else:
    print('Para juntar 1 milhão, voce precisa de {:.0f} meses ganhando {}'.format(ummilhao, (ummilhao/s), s))