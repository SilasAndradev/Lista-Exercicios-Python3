#Desafio 55  - Curso em Vídeo
#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for c in range(1, 6):
  peso = int(input('Digite o seu peso (em cm): ')) 
  if c == 1:
    maior = peso
    menor = peso
  if peso > maior:
    maior = peso
  if peso < menor:
    menor = peso
print('O menor peso é: {}, e o maior peso é: {}.'.format(menor, maior))
