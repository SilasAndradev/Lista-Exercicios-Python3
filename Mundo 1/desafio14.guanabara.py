#Desafio 14 - Curso em Vídeo
#Conversor de temperatura de Celsius para Fahrenheit ou vise-versa.
temp = float(input('Digite a temperatura: '))
mod = str(input('A temperatura é Celsius (C) ou Fahrenheit (F): '))
mood = str(input('É para converter em celsius (C) ou Fahrenheit (F): '))
if (mod == 'C') and (mood == 'C'):
  print('{}°C'.format(temp))
if (mod == 'F') and (mood == 'F'):
  print('{}°F'.format(temp))
if (mod == 'C') and (mood == 'F'):
  print('{}°F'.format((temp * 1.80) + 32))
if (mod == 'F') and (mood == 'C'):
  print('{}°C'.format((temp - 32)/ 1.8))
