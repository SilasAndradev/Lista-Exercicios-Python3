#Desafio 12 - Curso em Vídeo
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
precoNormal = float(input('Digite o preço do produto: '))
precoDesconto = precoNormal - precoNormal * 0.05
print('O produto que valia {}, com o desconto ira valer{}.'.format(precoNormal, precoDesconto))
