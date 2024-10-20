#Desafio 18 - Curso em Vídeo
#Faça um programa que leia o ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math
angulo = float(input('Digite o ângulo: '))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a tangente de {:.2f}.'.format(angulo, tangente))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem a cosseno de {:.2f}.'.format(angulo, cosseno))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem a seno de {:.2f}.'.format(angulo, seno))
