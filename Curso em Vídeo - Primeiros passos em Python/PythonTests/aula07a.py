n1 = int(input('Digite um número: '))
n2 = int(input('Outro número: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma vale {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end='')
print('A divisão inteira é {} e a potencia {}'.format(di, e))