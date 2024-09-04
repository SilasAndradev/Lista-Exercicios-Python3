#Desafio 70 - Curso em Video
import random
totalgasto = 0
produtos = 0
menor = 0
produtonome = ''
while True:
  nome = str(input('Digite o nome do produto: '))
  preco = float(input('Digite o preço do produto: '))
  print('='*20)
  totalgasto += preco
  if menor == 0:
    menor = preco
  if preco > 1000:
    produtos += 1
  if menor > preco:
    menor = preco
    produtonome = nome
  cont = str(input('Quer continuar? [S/N]: ')).upper()
  print('='*20)
  if cont == 'N':
    break
print(f'O total gasto foi R${totalgasto}\n{produtos} custam mais de 1000 reais\nO produto mais barato é {produtonome}')
