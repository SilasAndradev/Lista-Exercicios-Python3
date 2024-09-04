#Desafio 65 - Curso em Video
cont = 0
soma = 0
menor = 0 
maior = 0
media = 0
nue = 'S'
while nue == 'S':
  num = int(input('Digite um número: '))
  cont += 1
  soma += num
  if menor == 0:
    menor = num
  if menor > num:
    menor = num
  if maior < num:
    maior = num
  nue = str(input('Diga se você quer continuar [S/N]:')).upper()
media = soma / cont
print('A média dos números digitados é: {}. O maior valor é: {}. O menor valor é: {}'.format(media, maior, menor))
