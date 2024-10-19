import moeda

preço = float(input('Digite o preço: '))

print(f'O preço {moeda.moeda(preço)} aumentando 10% é igual: {(moeda.aumentar(preço, True))}')
print(f'O preço {moeda.moeda(preço)} diminuindo 10% é igual: {(moeda.diminuir(preço, True))}')
print(f'O preço {moeda.moeda(preço)} pela metade é igual: {(moeda.metade(preço, True))}')
print(f'O preço {moeda.moeda(preço)} dobrando é igual: {(moeda.dobro(preço, True))}')