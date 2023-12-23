dias = int(input('Quantos dias o carro foi alugado?'))
km = float(input('Quantos KM foram rodados com o carro?'))

valorDia = 60 * dias
valorKM = 0.15 * km
valorTotal = valorDia + valorKM

print('O carro que foi alugado para {} dias, rodou {:.2f}Km.\n O valor total à pagar ficou R${:.2f}.'.format(dias, km, valorTotal))
