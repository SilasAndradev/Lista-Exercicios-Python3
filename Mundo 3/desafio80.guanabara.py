#Desafio 80 - Curso em Video
valor = []
for i in range(0, 5):
  if len(valor) == 0:
    a = int(input('Digite um valor: '))
    valor.append(a)
    print('Você digitou o seu primeiro número.')
  else:
    a = int(input('Digite um valor: '))
    if a < min(valor):
      valor.insert(0, a)
      print(f'O valor {a} está sendo inserido na posição 0')
    elif a > max(valor):
      valor.append(a)
      print(f'O valor {a} está sendo inserido no final da lista.')
    else:
      j = 0
      while j < len(valor) and a >= valor[j]:
        j += 1
      valor.insert(j, a)
      print(f'O valor {a} está sendo inserido na posição {j}')
print('-='*20)
print(valor)
