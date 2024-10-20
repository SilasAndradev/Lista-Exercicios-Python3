#Desafio 40  - Curso em Vídeo
#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingido:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO
nota1 = float(input('Digite a nota 1 do aluno: '))
nota2 = float(input('Digite a nota 2 do aluno: '))
notaMedia = ((nota1 + nota2) / 2)
if (notaMedia < 5):
  print('Você foi REPROVADO.')
elif (notaMedia >= 5) and (notaMedia <= 6.9):
  print('Você está em RECUPERAÇÃO.')
elif (notaMedia >= 7):
  print('Você foi APROVADO.')
