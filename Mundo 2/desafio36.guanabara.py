#Desafio 36 - Curso em Vídeo
#Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
valorCasa = float(input('Digite qual é o valor da casa: '))
salarioComprador = float(input('Digite qual é o seu salário: '))
tempoAno = int(input('Digite em quantos anos você vai comprar a casa: '))
tempoMes = tempoAno * 12
if (valorCasa / tempoMes) > (salarioComprador * 0.30):
  print('O empréstimo foi negado por execeder 30% do salário do comprador. ')
else:
  print('O empréstimo foi aprovado, a prestação mensal será de: R${:.2f}'.format(valorCasa / tempoMes))
