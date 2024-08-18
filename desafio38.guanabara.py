#Desafio 38  - Curso em Vídeo
#Escreva uma programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#-O primeiro valor é maior
#-O segundo valor é maior
#Não existe valor maior, os dois são iguais.
num = int(input('Digite um número: '))
num2 = int(input('Digite um segundo número: '))
if (num > num2):
  print('O primeiro valor é maior.')
elif (num2 > num):
  print('O segundo valor é maior')
else:
  print('Não existe valor maior, os dois são iguais.')
