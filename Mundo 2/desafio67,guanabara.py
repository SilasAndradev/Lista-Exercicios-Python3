#Desafio 67 - Curso em Video
import random
meusPontos = 0
time = str(input('Você quer ser PAR ou IMPAR? ')).upper()
while True:
  n = int(input('Digite um número de 1 a 10: '))
  if 0 < n > 10:
    break
  comp = random.randint(1, 10)
  print(f'O computador pensou no número {comp}.')
  if ((time == 'PAR') and ((comp + n)% 2 != 0)) or ((time == 'IMPAR') and ((comp + n)% 2 == 0)):
    print('Você perdeu!')
    break
  else:
    meusPontos += 1
print(f'Você venceu {meusPontos} vezes consecutivas.')
