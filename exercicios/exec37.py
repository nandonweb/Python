c = int(input('Digite um numero inteiro: '))
escolha = int(input('Escolha entre binario, octal e hex: '))

if escolha == 1:
    print('Seu codigo em binario é {}'.format(bin(c)))
elif escolha == 2:
    print('Seu codigo em octal é {}'.format(oct(c)))
elif escolha == 3:
    print('Seu codigo em hexdecimal é {}'.format(hex(c)))
else:
    print('erro no codigo')