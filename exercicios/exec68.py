from random import randint
print('-='*10)
print('VAMOS JOGAR PAR E IMPAR')
print('-='*10)
v = 0
while True:
    valor = int(input('Digite um valor: '))
    computador = randint(0, 11)
    soma = computador + valor
    opcao = ' '
    while opcao not in 'PI':
     opcao = str(input('Par ou impar? [P/I]')).strip().upper()
     print(f'Voce jogou {valor} e o computador {computador}. Total de {soma}', end=' ')
     print('DEU PAR' if soma % 2 == 0 else 'DEU IMPAR')
    if opcao == 'P':
     if soma % 2 == 0:
        print('Voce Ganhou!')
        v += 1
     else:
        print('Voce Perdeu!!')
        break
    elif opcao == 'I':
     if soma % 2 == 1:
         print('Voce Ganhou!')
         v += 1
     else:
         print('Voce Perdeu!!')
         break
    print('='*10)
    print('Vamos jogar denovo')
print(f'GAME OVER! Você venceu {v} vezes.')

