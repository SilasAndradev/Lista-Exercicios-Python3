#Desafio 86 - Curso em Vídeo
matriz = [[], [], []]
for u in range(0, 3):
  for i in range(0, 3):
    matriz[u].append(int(input(f'Digite um para [{u}, {i}]')))
print('-='*30)
print(f'''[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]
[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]
[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]''')
