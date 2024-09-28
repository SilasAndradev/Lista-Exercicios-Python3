def area(largura, comprimento):
    área = largura * comprimento
    print(f'A área de um terreno {largura} * {comprimento} é de {área} m².')


print('Controle de Terrenos')
print('-='*20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
