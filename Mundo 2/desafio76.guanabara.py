#Desafio 76 - Curso em Vídeo
listagem = ('Molho de Tomate', 23.49, 'Chocolate', 3.49, 'Pão', 5, 'Feijão 1KG', 20.97, 'Arroz 1KG', 7.99)
print('-'*50)
print('{:^50}'.format('Mercadinho do Seu Zé'))
print('-'*50)
for c in range(0, len(listagem), 2):
  print(f'{listagem[c]:.<40}R${listagem[c+1]:>8.2f}')
print('=' * 50)
