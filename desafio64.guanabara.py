#Desafio 64 - Curso em Video
cont = 0
soma = 0
num = 0
while num != 999:
  num = int(input('Digite um número: '))
  soma += num
  cont += 1
print('A soma dos valores digitados são: {}, e a quantidade é de valor digitados são {}'.format(soma - 999, cont))
