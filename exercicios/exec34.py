n = int(input('Qual seu salario: '))

porcem = n + (n * 10 / 100)
porcem2 = n + (n * 15 / 100)

if n >= 1250:
    print('Aumento de 10% = {:.2f} Reais'.format(porcem))
else:
    print('Aumento de 15% = {:.2f} Reais'.format(porcem2))