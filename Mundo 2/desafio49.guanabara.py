#Desafio 49  - Curso em Vídeo
#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora ultilizando um laço for.
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 10 + 1):
  print(num, '*', c, '=', num * c)
