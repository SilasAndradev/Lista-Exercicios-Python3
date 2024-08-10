#Desafio 15 - Curso em Vídeo
km = float(input('Digite quantos Kilometros rodou: '))
dia = float(input('Digite quantos dias rodou: '))
precoPagar = (dia * 60) + (km * 0.15)
print('O total a ser pago será de R$ {}'.format(precoPagar))
