#Desafio 11 - Curso em Vídeo
#Faça um programa que leia a largura e a altura de um parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
largura = float(input('Digite a largura da parede que irá pintar: '))
altura = float(input('Digite a altura da parede que irá pintar: '))
area = altura * largura
print('A quantidade de tinta que será necessária para pintar a parede de {} m², será de {} litros.'.format(area, area / 2))
