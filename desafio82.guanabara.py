#Desafio 82 - Curso em Video
valor = []
valor1 = []
valor2 = []
while True:
  a = int(input('Digite um número: '))
  valor.append(a)
  keep = str(input('Quer continuar [SIM/NÃO]: ')).upper().strip()
  if keep[0] == 'N':
    break
  elif keep[0] == 'S':
    print('Continuando...')
  else: 
    print('Digite corretamente na próxima vez: ')
for j, v in enumerate(valor):
  if v % 2 == 0:
    valor2.append(v)
  else:
    valor1.append(v)
print(f'A lista normal é: {valor}')
print(f'A lista somente com os números ímpares são: {valor1}')
print(f'A lista somente com os números pares são: {valor2}')
