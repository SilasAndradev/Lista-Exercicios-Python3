#Desafio 57 - Curso em Video
#Faça um programa que leia o sexo de uma pessoa, mas só aceita os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
c = 0
while c < 1:
  sexo = str(input('Digite seu sexo [M/F]:')).upper()
  if sexo == 'M' or sexo == 'F':
    c += 1
  else:
    print('Repita')
if sexo == 'M':
  print("Seu sexo é masculino")
if sexo == 'F':
  print("Seu sexo é feminino")
