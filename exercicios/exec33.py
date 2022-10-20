n = int(input('Digite primeiro numero: '))
n2 = int(input('Digite segundo numero: '))
n3 = int(input('Digite terceiro numero: '))

if n or n2 or n3 > n & n2 & n3:
    print('{} é maior que {} e {}'.format(n, n2, n3))
else:
    print('erro')

