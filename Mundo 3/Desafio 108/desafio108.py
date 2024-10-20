import moeda

preço = float(input('Digite o preço: '))

print(f'O preço {moeda.moeda(preço)} aumentando 10% é igual: {moeda.moeda(moeda.aumentar(preço))}')
print(f'O preço {moeda.moeda(preço)} diminuindo 10% é igual: {moeda.moeda(moeda.diminuir(preço))}')
print(f'O preço {moeda.moeda(preço)} pela metade é igual: {moeda.moeda(moeda.metade(preço))}')
print(f'O preço {moeda.moeda(preço)} dobrando é igual: {moeda.moeda(moeda.dobro(preço))}')