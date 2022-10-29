from random import randint
pc = randint(0, 11)
print('Acabei de pensar em um numero de 0 a 10')
print('Sera que voce advinhar qual foi? ')
palpite = 0
acertou = False
while not acertou:
    jogador = int(input('Qual é o palpite: '))
    palpite += 1
    if jogador == pc:
       acertou = True
    else:
        if jogador < pc:
            print('Mais... Ta perto')
        elif jogador > pc:
            print('Menos... Ta perto ')
print('Voce acertou com {} tentativas, Parabens!'.format(palpite))

