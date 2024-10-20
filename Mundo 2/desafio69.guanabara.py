#Desafio 69 - Curso em Video
import random
cont = 0
contHom = 0
contmu = 0
while True:
  sexo = str(input('Digite qual é o seu sexo [M/F]: ')).upper()
  idade = int(input('Digite a sua idade: '))
  if idade > 18:
    cont += 1
  if sexo == 'M':
    contHom += 1
  if idade < 20:
    contmu += 1
  continua = str(input('Você deseja continuar? [S/N]: ')).upper()
  if continua == 'N':
    break
print(f'Das pessoas que foram cadastrados(as) {cont} tem mais de 18 anos, {contHom} foi homens e {contmu} foi mulheres com menos de 20 anos.')
