#Desafio 66 - Curso em Video
soma = 0
cont = 0
while True:
  n = int(input('Digite um número: '))
  if n == 999:
    break
  soma += n
  cont += 1
print(f'A soma de todos os números digitados é {soma} e a quantidade de números digitados é {cont}')
