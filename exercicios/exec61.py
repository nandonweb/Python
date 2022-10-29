print('Sequencia de fibonacci')
n = int(input('Quantos termos voce quer mostar: '))
a = 0
b = 1
print('~'*20)
print('{} → {}'.format(a, b), end='')
cout = 3
while cout <= n:
    c = a + b
    print(' → {}'.format(c), end='')
    a = b
    b = c
    cout += 1
print(' → FIM')
print('~'*20)
