#Desafio 37 - Curso em Vídeo
#Escreva um programa que leia um número inteiro qualquer e peça para usuário escolher qual será a base da conversão:
#-1 para binário
#-2 para octal
#-3 para hexadecimal
num = int(input('Digite um número: '))
base = int(input('Digite qual será a base da conversão:\n-1 para binário\n-2 para octal\n-3 para hexadecimal\n'))
if (base == 1):
  print(bin(num)[2:])
elif (base == 2):
  print(oct(num)[2:])
elif (base == 3):
  print(hex(num)[2:])
