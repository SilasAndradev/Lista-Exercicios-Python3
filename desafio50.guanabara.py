#Desafio 50  - Curso em Vídeo
#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que foram pares. Se o valor digitado for ímpar, desconsidere-o
soma = 0
for c in range(1, 6):
  num = int(input('Digite um número: '))
  if num % 2 == 0:
    soma = soma + num
print('A soma de todos os números pares são',soma)
