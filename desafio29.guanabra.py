#Desafio 29 - Curso em Vídeo
#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapssar 80Km/h, mostre uma mensagem dizendo que foi multado.
#A multa vai custa R$7.00 por cada Km acima do limite.
metros = float(input('Digite qual foi a distância pecorrida: '))
s = float(input('Digite em quanto tempo ele fez o trajeto (em segundos): '))
velocidade = metros / s
velocidadeMulta = velocidade - 80
if velocidade <= 80 :
  print('Você não foi multado. ')
else: 
  print('Você foi multado em {}, por está a {} Km/h'.format(velocidadeMulta * 7, velocidade))
