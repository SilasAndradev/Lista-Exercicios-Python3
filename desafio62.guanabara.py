#Desafio 62 - Curso em Video
razao = int(input('Digite a razão da sua progressão aritmética: '))
primter = int(input('Digite o primeiro termo da sua progressão aritmética: '))
cont = 1
while cont < 11:
  primter += razao
  print(primter)
  cont+=1
num = int(input('Você quer que o programa mostre mais termos? Se sim diga quantos, se não diga 0: '))
if num > 0:
  while num > 0:
    primter += razao
    print(primter)
    num -= 1
