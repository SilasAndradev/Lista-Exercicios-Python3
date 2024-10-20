#Desafio 31 - Curso em Vídeo
#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km e R$0.45 para viagens mais longas.
distancia = float(input('Digite a distância pecorrida (em KM): '))
if distancia <= 200:
  print('O preço da passagem custa R${}'.format(distancia * 0.50))
else:
  print('O preço da passagem custa R${}'.format(distancia * 0.45))
