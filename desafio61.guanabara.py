#Desafio 61 - Curso em Video
razao = int(input('Digite a razão da sua progressão aritmética: '))
primter = int(input('Digite o primeiro termo da sua progressão aritmética: '))
cont = 1
num = 1
while cont < 11:
  primter += razao
  print(primter)
  cont+=1
