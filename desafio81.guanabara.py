#Desafio 80 - Curso em Video
valor = []
v = 0
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
  if 5 in valor:
    v = 1
print(f'Foram digitados {len(valor)} números na lista.')
valor.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valor}')
if v == 1:  
  print('O valor 5 foi digitado.')
else:
  print('o valor 5 não foi digitdo.')
