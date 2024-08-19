#Desafio 39  - Curso em Vídeo
#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#- Se ele ainda vai se alistar ao serviço militar.
#- Se é a hora de se alistar.
#- Se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
anoNasc = int(input('Digite o ano em que nasceu: '))
anoAtual = date.today().year
idade = anoAtual - anoNasc
if idade < 18:
  saldo = 18 - idade
  print('Ainda faltam {} anos para o alistamento'.format(saldo))
  ano = anoAtual + saldo
  print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
  saldo = idade - 18
  print('Você deveria ter se alistado há {} anos'.format(saldo))
  ano = anoAtual - saldo
  print('Seu alistamento foi em {}.'.format(ano))
elif idade == 18:
  print('Já está na hora de se alistar.') 
