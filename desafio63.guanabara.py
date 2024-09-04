#Desafio 63 - Curso em Video
cont = 1
ultimo = 1
penultimo = 1
termo = 1
num = int(input('Digite um número: '))
if (num==1):
  print("0")
elif (num==2):
  print('0 -> 1')
else:
  while cont <= num:
    if termo == 1:
      print('0 ->',termo, end=' -> ')
      termo += 1
    else:
      termo = ultimo + penultimo 
      penultimo = ultimo
      ultimo = termo  
      cont += 1
      print(termo, end=' -> ')
