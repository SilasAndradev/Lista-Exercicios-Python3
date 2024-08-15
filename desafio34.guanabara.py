#Desafio 34 - Curso em Vídeo
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250, calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%
salario = float(input('Digite qual é seu salário: '))
if salario > 1250.00:
    print('O seu salário que era de R${}, após o aumento será de R${}'.format(salario, salario + (salario * 0.1)))
if salario <= 1250.00:
    print('O seu salário que era de R${}, após o aumento será de R${}'.format(salario, salario + (salario * 0.15)))
