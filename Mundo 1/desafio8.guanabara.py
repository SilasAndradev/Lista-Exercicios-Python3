#Desafio 8 - Curso em Vídeo
#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
metros = float(input('Digite um valor para ser convertido: '))
centiMetros = metros*100
miliMetros = centiMetros*10
print('O valor de {} em centímetros é de: {}\nO valor de {} em milímetros é de: {}'.format(metros, centiMetros, metros, miliMetros))
