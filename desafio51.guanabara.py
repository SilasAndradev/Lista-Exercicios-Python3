#Desafio 51  - Curso em Vídeo
#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão:
num1 = int(input('Digite o primeiro termo da sua progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))
for i in range(1, 10):
  print(num1 + i * razao)
