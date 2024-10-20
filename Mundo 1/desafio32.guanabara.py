#Desafio 31 - Curso em Vídeo
#Faça um programa que leia um ano qualquer e mostre se ela é Bissexto.
ano = int(input('Digite o ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é Bissexto!')
else:
    print('O ano não é Bissexto!')
