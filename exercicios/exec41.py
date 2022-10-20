from datetime import date

i = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
ano = 2022 - i

if ano <= 9:
    print('Voce tem {} anos e é MIRIM'.format(ano))
elif ano <= 14:
    print('Voce tem {} anos e é INFATIL'.format(ano))
elif ano <= 19:
    print('Voce tem {} anos e é JUNIOR'.format(ano))
elif ano <= 25:
    print('Voce tem {} anos e é SENIOR'.format(ano))
else:
    print('Voce tem {} anos e é MASTER'.format(ano))