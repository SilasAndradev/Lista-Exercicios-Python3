#Desafio 42  - Curso em Vídeo
#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado
#- Equilátero: todos os lados iguais
#- Isósceles: dois lados iguais
#- Escaleno: todos os lados diferente
ladoA = float(input('Digite o lado A do triângulo: '))
ladoB = float(input('Digite o lado B do triângulo: '))
ladoC = float(input('Digite o lado C do triângulo: '))
if ladoA < ladoB + ladoC and ladoB < ladoA + ladoB and ladoC < ladoA + ladoB:
    print('As três retas PODEM FORMAR um triângulo.')
    if ladoA == ladoB and ladoB == ladoC:
      print('O triângulo formado é um Equilátero.')
    elif ladoC != ladoA and ladoA != ladoB:
      print('O triângulo formado é um Escaleno.')
    elif ladoB in (ladoC, ladoA):
      print('O triângulo formado será um Isósceles.')
else:
    print('As três retas NÃO PODEM formar um triângulo.')
