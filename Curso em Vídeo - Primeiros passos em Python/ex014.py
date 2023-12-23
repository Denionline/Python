temp = float(input('Informe uma temperatura: '))
tipo = input('Escreva C para Celsius, e F para Farheinheit: ')

if tipo == 'F':
    conversão = (temp - 32) * 5/9
    print('A temperatura {:.1f}ºF, convertida para Celsius, fica {:.4f}ºC.'.format(temp, conversão))
else:
    conversão = (temp * 9/5) + 32
    print('A temperatura {:.4f}ºC, convertida para Farheinheit, fica {:.1f}ºF.'.format(temp, conversão))
    
