maior = 0
menor = 0
for c in range(1, 8):
    pessoas = int(input('Digite seu ano de nascimento: '))
    ok = 2022 - pessoas
    if ok >= 21:
        maior += 1
    else:
        menor += 1
print('{} pessoas são maiores de idade'.format(maior))
print('{} pessoas ainda são menores'.format(menor))