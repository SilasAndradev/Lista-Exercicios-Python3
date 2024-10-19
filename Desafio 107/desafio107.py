import moeda

preço = float(input('Digite o preço: '))

print(f'O preço {preço} aumentando 10% é igual: {moeda.aumentar(preço)}')
print(f'O preço {preço} diminuindo 10% é igual: {moeda.diminuir(preço)}')
print(f'O preço {preço} pela metade é igual: {moeda.metade(preço)}')
print(f'O preço {preço} dobrando é igual: {moeda.dobro(preço)}')