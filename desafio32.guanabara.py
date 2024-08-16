#Desafio 32 - Curso em Vídeo
#Faça um programa que leia um ano qualquer e mostre se ela é Bissexto.
ano = int(input('Digite o ano: '))
if ano % 4 == 0 and ano % 100 != 0:
    print('Na primeira situação: O ano é Bissexto!')
else:
    print('Na primeira situação: O ano não é Bissexto!')
if ano % 4 != 0 and ano % 400 != 0:
  print('Na segunda situação: O ano não é Bissexto!')
else:
    print('Na segunda situação: O ano é Bissexto!')
