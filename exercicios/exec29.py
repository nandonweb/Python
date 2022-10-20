v = int(input('Qual a velocidade do carro: '))

multa = (v-80) * 7

if v > 80:
    print('Voce Foi Multado em {} reais'.format(multa))
else:
    print('Continue assim!')