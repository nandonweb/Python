p = float(input('Digite seu peso: '))
a = float(input('Digite sua altura: '))

imc = (p / a**2)

if imc <= 18.5:
    print('seu imc é {:.0f}, e voce esta abaixo do peso normal'.format(imc))
elif imc >= 18.6 and imc <= 24.9:
    print('seu imc é {:.0f}, e voce esta com peso normal'.format(imc))
elif imc >= 25.0 and imc <= 29.9:
    print('seu imc é {:.0f}, e voce esta com excesso de peso'.format(imc))
elif imc >= 30.0 and imc <= 34.9:
    print('seu imc é {:.0f}, e voce esta com obesidade classe I'.format(imc))
elif imc >= 35.0 and imc <= 39.9:
    print('seu imc é {:.0f}, e voce esta com obesidade classe II'.format(imc))
elif imc >= 40:
    print('seu imc é {:.0f}, e voce esta com obesidade classe III'.format(imc))