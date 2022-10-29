while True:
    t = int(input('Qual tabuada deseja ver: '))
    if t <= -1:
        break
    for x in range(1, 11):
        print(f'{t} X {x} = {t*x}')
print('Programa Encerrado.')
