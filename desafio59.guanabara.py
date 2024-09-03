#Desafio 59 - Curso em Video
import random
c = 0
while c < 1:
  num1 = float(input('Digite um valor: '))
  num2 = float(input('Digite um segundo valor: '))
  menu = int(input('Digite um número para fazer cada ação:\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\n'))
  if menu == 1:
    print('A soma do valor {} e o valor {} é: {}'.format(num1, num2, num1 + num2))
    c += 1
  elif menu == 2:
    print('A multiplicação do valor {} e o valor {} é: {}'.format(num1, num2, num1 * num2))
    c +=1
  elif menu == 3:
    if num1 > num2:
      print('O valor {} é maior que o valor {}'.format(num1, num2))
    elif num1 < num2:
      print('O valor {} é maior que o valor {}'.format(num2, num1))
      c +=1
  elif menu == 4:
    print('Aqui está os novos números: ')
  elif menu == 5:
    print('Bye, Bye')
    c += 1
  else:
    print("Você digitou um número errado. ")
