#Desafio 28 - Curso em Vídeo
#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o núemro escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
from time import sleep
num = random.randint(0, 5)
num2 = int(input('Digite um número de 0 a 5: '))
print('PROCESSANDO...')
sleep(5)
if num2 == num:
  print('Você acertou! Eu pensei no número {}.'.format(num))
else:
  print('Você errou! Eu pensei no número {}.'.format(num))
