#Desafio 46  - Curso em Vídeo
#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício de 10 a 0, com uma pausa de 1 segundo entre eles.
import time
print('Os fogos irão estourar em:')
for c in range(10, -1, -1):
  print(c)
  time.sleep(1)
print('Kabuuuum!!!')
