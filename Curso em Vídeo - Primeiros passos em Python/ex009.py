numero = int(input('Insira um número: '))

print(f'A tabuada do número {numero} é:', end='')
c = 0
while (c <= 10):
    print(f'{c} x {numero} = {c * numero}')
    c += 1