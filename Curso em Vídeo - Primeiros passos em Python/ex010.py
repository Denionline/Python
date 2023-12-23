valorReal = float(input('Insira um valor em real: R$'))

valorDolar = 3.27

print('O valor que você inseriu de R$ {:.2f}, pode comprar $ {:.2f} dolares.'.format(valorReal, valorReal / valorDolar))