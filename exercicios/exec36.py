casa = int(input('Digite o valor da casa: R$'))
salario = int(input('Digite seu salario: R$'))
anos = int(input('Em quantos anos voce vai pagar: '))
prestacao = (casa / anos) / 12
porcem = salario * 30 / 100
if prestacao > porcem:
    print('Seu empretimo foi NEGADO!')
else:
    print('Seu empretimo foi APROVADO!, com a parcela de R${:.2f} durante {} anos'.format(prestacao, anos))
