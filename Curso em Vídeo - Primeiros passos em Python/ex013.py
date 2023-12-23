salario = float(input('Qual salário do funcionário? R$'))

porcentagem = 15 / 100
valorParaAumentar = salario * porcentagem

print('O salário atual do funcionário é R${:.2f} foi promovido, e recebeu 15% de aumento, ficando com um novo salário de R${:.2f}!'.format(salario, salario + valorParaAumentar))