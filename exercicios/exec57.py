sexo = str(input('Informe seu sexo: [M/F] ')).strip()
while sexo not in 'MnFf':
    sexo = str(input('Dados invalidos, Informe seu Sexo [M/F]: ')).upper().strip()
print('Sexo {} registrado com sucesso'.format(sexo))