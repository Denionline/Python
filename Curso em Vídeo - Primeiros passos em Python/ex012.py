valor = float(input('Informe um valor: R$'))

desconto = 5
valorDoAbatimento = valor * desconto / 100

print('O valor R${:.2f} com o desconto de 5%, é de R${:.2f}.'.format(valor, valor - valorDoAbatimento))