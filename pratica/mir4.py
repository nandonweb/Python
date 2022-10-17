# Calculadora Mir4 = Aco Negro

miner = int(input('Em Quantos Segundos Você Minera? '))
dsporvez = int(input('Media de Dark Steel Minerado por Vez? '))
tempor = int(input('Tempo Restante em Minuto? '))

tempoMinerada = 60 / miner
calculo = tempoMinerada * dsporvez
tempoRestante = calculo * tempor

# time
tempo = calculo * 60
meiodia = tempo * 12
dia = tempo * 24

print('='*30)
print('Seu Farm Restante - {:,.0f} Dark Steel'.format(tempoRestante).replace(',', '.'))
print('1 Minuto - {:,.0f} Dark Steel'.format(calculo).replace(',', '.'))
print('1 Hora - {:,.0f} Dark Steel'.format(tempo).replace(',', '.'))
print('12 Horas - {:,.0f} Dark Steel'.format(meiodia).replace(',', '.'))
print('24 Horas - {:,.0f} Dark Steel'.format(dia).replace(',', '.'))
