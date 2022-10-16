a = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

aluguel = 60
porkm = 0.15
calc = (a * aluguel) + (km * porkm)

print('o total a pagar é de R${:.2f}'.format(calc))

