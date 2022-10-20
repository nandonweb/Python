from datetime import date

nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nascimento
alistamento = idade - 18
atraso_alistamento = ano_atual - alistamento

if idade < 18:
    saldo = 18 - idade
    futuro_alistamento = ano_atual + saldo
    print('Você tem {} anos e ainda falta {} anos para se alistar, voce ira se alistar em {}'.format(idade, saldo, futuro_alistamento))
elif idade == 18:
    print('voce tem {} anos, è hora de se alistar'.format(idade))
else:
    print('voce tem {} anos, voce ja deveria ter se alista há {} anos, seu alistamento foi em {}'.format(idade, alistamento, atraso_alistamento))
