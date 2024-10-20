#Desafio 67 - Curso em Video
while True:
  c = 0
  n = int(input('Quer ver a tabuada de qual valor? '))
  print("-" * 20)
  if n <= 0:
    break
  while c < 11:
    print(f'{n} * {c} = {n * c}')
    c += 1
  print("-" * 20)
