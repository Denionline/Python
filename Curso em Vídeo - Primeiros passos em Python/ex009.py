numero = int(input('Insira um número: '))

print(f'A tabuada do número {numero} é:')
print(f'-' * 12)
c = 0
while (c <= 10):
    print(f'{numero} x {c:2} = {c * numero}')
    c += 1
print(f'-' * 12)    