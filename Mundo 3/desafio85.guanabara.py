#Desafio 85 - Curso em Vídeo
valores = [[], []]
for p in range(1, 8):
  valor = int(input(f'Digite o {p}° valor: '))
  if valor % 2 == 0:
    valores[0].append(valor)
  else:
    valores[1].append(valor)
print(f'Os valores pares digitados foram: {sorted(valores[0])}')
print(f'Os valores impares digitados foram: {sorted(valores[1])}')
