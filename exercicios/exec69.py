contador_maioridade = contador_homens = contador_mulheres_mais20 = 0

while True:
    print('\033[;36m-\033[m' * 30)
    print('     \033[1;97mCADASTRE UMA PESSOA')
    print('\033[;36m-\033[m' * 30)

    idade = int(input('\033[1;97mIdade:\033[m '))
    while True:
        sexo = str(input('\033[1;97mSexo [M/F]:\033[m ')).strip().upper()
        if sexo not in 'MF':
            print('\033[;31mOpção Inválida! Tente de novo.\033[m')
        else:
            break

    if idade >= 18:
        contador_maioridade += 1
    if sexo == 'M':
        contador_homens += 1
    if sexo == 'F' and idade < 20:
        contador_mulheres_mais20 += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('\033[1;97mQuer continuar? [S/N]:\033[m ')).strip().upper()
        if continuar not in 'SN':
            print('\033[;31mOpção Inválida! Tente de novo.\033[m')
    if continuar == 'N':
        break

print('-'*30)
print(f'Total com +18: {contador_maioridade}')
print(f'Total de homens: {contador_homens}')
print(f'Total de mulheres com menos de 20 anos: {contador_mulheres_mais20}')
print('-'*30)