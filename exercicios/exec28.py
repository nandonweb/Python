from random import randint
from time import sleep
pc_num = randint(0, 5)
print('Vou pensar em um numero de 0 a 5, tente adivinhar')
print('-=-'*20)
jogador = int(input('em que numero eu pensei? '))
print('Processando...')
sleep(2)
if jogador == pc_num:
    print('Parabens')
else:
    print('ganhei! eu pensei no numero {} e nao no {}'.format(pc_num, jogador))