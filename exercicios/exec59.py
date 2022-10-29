from time import sleep
opcao = 0
while opcao != 5:
    x = int(input('Primeiro valor: '))
    y = int(input('Segundo valor: '))
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos numeros')
    print('[ 5 ] sair do programa')
    opcao = int(input('Qual sua opcao: '))
    if opcao == 1:
        print('-==-'*10)
        print('o Resultado foi', x+y)
    elif opcao == 2:
        print('-==-'*10)
        print('o Resultado foi', x*y)
    elif opcao == 3:
        print('-==-' * 10)
        if x > y:
            maior = x
        else:
            maior = y
        print('o Resultado foi', maior)
    elif opcao == 4:
        print('informe os numeros novamente: ')
        x = int(input('Primeiro Valor: '))
        y = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(2)
        print('*' * 15)
        print('Fim do Programa')
    else:
        print('Opção invalida')