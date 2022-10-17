f = input('Digite uma frase: ').upper()

print('a letra A aparece {} vezes'.format(f.count('A')))
print('a primeira letra A aparece na posicao {}'.format(f.find('A')))
print('a ultima letra A aparece na posicao {}'.format(f.rfind('A')))