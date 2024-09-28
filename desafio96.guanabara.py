def area(l, c):
    área = l * c
    print(f'A área de um terreno {l} * {c} é de {área} m².')


print('Controle de Terrenos')
print('-='*20)

area(l = float(input('LARGURA (m): ')),
    c = float(input('COMPRIMENTO (m): ')))
