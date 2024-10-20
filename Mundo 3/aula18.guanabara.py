#Aula 18 - Curso em Vídeo
#teste = list()
#teste.append('Gustavo')
#teste.append(25)
#galera = list()
#galera.append(teste) Quando faço isso, cria uma ligação entre as duas listas
#galera.append(teste[:])  #Já aqui, eu crio uma cópia

galera = [['João', 19], ['Ana', 33], ['Maria', 45]]
#print(galera[2][1]) #Mostra 45
totmai = totmen = 0
#for p in galera:
#  print(f'{p[0]} tem {p[1]} anos de idade')
galera1 = list()
dado = list()

for c in range(0, 3):  #Cria 3 listas dado na lista galera com nome e idade 
  dado.append(str(input('Nome: ')))
  dado.append(int(input('Idade: ')))
  galera1.append(dado[:])  #Não pode esquercer isso
  dado.clear()
print(galera1)

for j in galera:
  if j[1] >= 21:
    print(f'{j[0]} é maoir de idade.')
    totmai += 1
  else:
    print(f'{j[0]} é menor de idade.')
    totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores')
