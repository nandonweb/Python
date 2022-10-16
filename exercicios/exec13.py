s = float(input('Qual seu salario: '))

aumento = 15
novo = s + (s * aumento / 100)

print('o seu salario de R${} aumentou para R${}'.format(s, novo))
