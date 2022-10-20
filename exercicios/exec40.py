n = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n + n2) / 2

if media < 5.0:
    print('Voce tirou {} e foi Reprovado'.format(media))
elif media >= 5.0 and media < 7:
    print('Voce tirou {} e esta de Recuperacao'.format(media))
else:
    print('Voce tirou {} e foi Aprovado'.format(media))
