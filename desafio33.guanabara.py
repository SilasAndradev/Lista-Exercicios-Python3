#Desafio 33 - Curso em Vídeo
#Faça um programa que leia três números e mostre qual é o maior e qual o menor
num1 = float(input('Digite um número: '))
num2 = float(input('Digite um número: '))
num3 = float(input('Digite um número: '))
if num1 > num2 and num2 > num3:
    print('{} é o maior e {} é o menor'.format(num1, num3))
if num1 > num3 and num3 > num2:
    print('{} é o maior e {} é o menor'.format(num1, num2))
if num2 > num1 and num1 > num3:
    print('{} é o maior e {} é o menor'.format(num2, num3))
if num2 > num3 and num3 > num1:
    print('{} é o maior e {} é o menor'.format(num2, num1))
if num3 > num2 and num2 > num1:
    print('{} é o maior e {} é o menor'.format(num3, num1))
if num3 > num1 and num1 > num2:
    print('{} é o maior e {} é o menor'.format(num3, num2))
