#Desafio 6 - Curso em Vídeo
#Faça um programa que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um número: '))
r = n ** (1/2)
d = n * 2
t = n * 3
print('A triplo de {} é {}\nO seu dobro é {}\nE a raiz quadrada é {}'.format(n, t, d, r))
