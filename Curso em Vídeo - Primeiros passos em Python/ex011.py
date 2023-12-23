altura = float(input('Insira a altura da parede: '))
largura = float(input('Insira a largura da parede: '))

metrosQ = altura * largura
qtdeTinta = metrosQ / 2

print('A altura da parede é {}, e a largura {}, então temos {:.2f}m², e a quantidade de tinta para pintar essa parede é de {:.4f}L.'.format(altura, largura, metrosQ, qtdeTinta))

