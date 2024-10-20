#Desafio 41  - Curso em Vídeo
#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima: MASTER
from datetime import date
ano = int(input('Digite em que ano você nasceu: '))
anohj = date.today().year
if ((anohj - ano) <= 9):
  print('Sua categoria é: MIRIM.')
elif ((anohj - ano) <= 14):
  print('Sua categoria é: INFANTIL.')
elif ((anohj - ano) <= 19):
  print('Sua categoria é: JÚNIOR.')
elif ((anohj - ano) <= 25):
  print('Sua categoria é: SÊNIOR.')
else:
  print('Sua categoria é: MASTER.')
