#Desafio 54  - Curso em Vídeo
#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
acum = 0
acum1 = 0
for c in range(1, 8):
  num = int(input('Digite o ano do seu nascimento: '))
  if 2024 - num >= 18:
    acum = acum + 1
  if 2024 - num < 18:
    acum1 = acum1 + 1
print('{} pessoas já são de maior e {} ainda não são de maior.'.format(acum, acum1))
