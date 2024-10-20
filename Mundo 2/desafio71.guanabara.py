#Desafio 71 - Curso em Video
cedula50 = 0
cedula20 = 0
cedula10 = 0
cedula5 = 0
while True:
  num = int(input('Digite o valor a ser sacado: '))
  if num >= 5:  
    if num >= 50:
      cedula50 = num // 50
      if cedula50 * 50 != num:
        cedula20 = (num - cedula50 * 50) // 20
        if (cedula20 * 20) + (cedula50 * 50) != num:
          cedula10 = (num - (cedula50 * 50) - (cedula20 * 20)) // 10
          if (cedula20 * 20) + (cedula50 * 50) + (cedula10 * 10) != num:
            cedula5 = (num - (cedula50 * 50) - (cedula20 * 20) - (cedula10 * 10)) // 5
    elif num >= 20:
      cedula20 = num // 20
      if cedula20 * 20 != num:
        cedula10 = (num - cedula20 * 20) // 10
        if (cedula20 * 20) + (cedula50 * 10) != num:
          cedula5 = (num - (cedula20 * 20) - (cedula10 * 10)) // 5
    elif num >= 10:
      cedula10 = num // 10
      if cedula10 * 10 != num:
       cedula5 = (num - cedula10 * 10) // 5
  break
print(f'Será entrege {cedula50} cédulas de R$50, {cedula20} cédulas de R$20, {cedula10} cédulas de R$10 e {cedula5} cédulas de R$5.')
