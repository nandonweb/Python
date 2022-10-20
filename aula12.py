nome = str(input('Qual seu nome: '))

if nome == 'Fernando':
    print('Que nome bonito')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Joao':
    print('Belo nome!')
elif nome in 'Ana Clauida Jessica Juliana':
    print('Belo nome feminino')
else:
    print('seu nome é bem normal')
print('Bom dia, {}'.format(nome))