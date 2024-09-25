#Desafio 87 - Curso em Vídeo
matriz = [[], [], []]
pares = 0
valorTC = 0
maior = 0

for u in range(0, 3):
  
  for i in range(0, 3):
    matriz[u].append(int(input(f'Digite um para [{u}, {i}]: ')))
    
    if matriz[u][i] % 2 == 0:
      pares += matriz[u][i]

for j in range(0,3):
  valorTC += matriz[j][2]

for f in range(0,3):
  
  if matriz[1][f] > maior:
    maior = matriz[1][f]

print('-='*30)
print(f'''[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]
[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]
[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]''')
print('-='*30)
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {valorTC}')
print(f'O maior valor da segunda linha é {maior}')