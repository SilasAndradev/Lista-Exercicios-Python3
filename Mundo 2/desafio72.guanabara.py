#Desafio 72 - Curso em Video
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
  num = int(input('Digite um número de 0 a 20: '))
  if -1 < num < 21:
    print(f'Você digitou o número: {numeros[num]}')
    break
  else:
    print('Tente novamente')
