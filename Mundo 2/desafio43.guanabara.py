#Desafio 43  - Curso em Vídeo
#Desenvolva uma lógica que leia o peso  a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal 
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura (em metros): ')) 
imc = peso / (altura * altura)
if imc < 18:
  print('Você está abaixo do peso.')
elif imc >= 18.5 and imc <= 25:
  print('Você está no peso ideal.')
elif imc >= 26 and imc <= 30:
  print('Você está em Sobrepeso.')
elif imc >= 31 and imc <= 40:
  print('Você está com Obesidade.')
elif imc > 40:
  print('Você está com Obesidade Mórbida.')
