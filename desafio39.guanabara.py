#Desafio 39  - Curso em Vídeo
#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#- Se ele ainda vai se alistar ao serviço militar.
#- Se é a hora de se alistar.
#- Se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime
from datetime import date
ano = int(input('Digite o ano em que nasceu: '))
mes = int(input('Digite o mês em que nasceu: '))
dia = int(input('Digite o dia em que nasceu: '))
dataNasc = datetime.date(year=ano, month=mes, day=dia) 
diferenca = date.today() - dataNasc
if (diferenca.days / 365.25) > 18:
  print('O prazo do alistamento já passou em {} dias'.format(diferenca.days - 6574.5))
elif (diferenca.days / 365.25) < 18:
  print('Ainda faltam {} dias para o alistamento'.format(6574.5 - diferenca.days))
elif (diferenca.days / 365.25) == 18:
  print('Já está na hora de se alistar.') 
