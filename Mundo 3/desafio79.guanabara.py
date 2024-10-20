#Desafio 79 - Curso em Video
valor = []
while True:
  a = int(input('Digie um valor: '))
  if a in valor:
    print('O valor já está na lista')
  else:
    valor.append(a)
  keep = str(input('Quer continuar [SIM / NÃO]?')).upper().strip()
  if keep[0] == 'S':
    print('Continuando')
  elif keep[0] == 'N':
    break
  else:
    print("Apenas digite 'sim' ou 'não'!")
print(f'Você digitou os valores {valor}.')
