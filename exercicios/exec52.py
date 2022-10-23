n1 = int(input('Digite um numero: '))
divisor = 0
for count in range(1, n1+1):
    if n1 % count == 0:
        divisor += 1
if divisor == 2:
    print(f'primo com apenas {divisor} números divisíveis por {n1}.')
else:
    print(f'Não é primo, pois tem {divisor} números divisíveis por {n1}.')