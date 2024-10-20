#Aula 17 - Curso em Vídeo

#Tupla
#num = (2, 5, 9, 1)   
#num [2] = 3 Isso não é possivel, pois as tuplas são imutáveis

#Lista
num = [2, 5, 9, 1] 
num[2] = 3

num.append(7) 
#Adiciona mais um número no final da lista

num.sort() 
#Deixar a lista em ordem

num.sort(reverse=True) 
#Deixar a lista em ordem reversa

num.insert(2, 0) 
#Vai adicionar o número 0 na posição 2

num.pop() 
#Sem nenhum número no parâmetro ele vai excluir o último valor da lista.
#Se houver algum número será a posição em que será excluido algum número.

num.remove(2)
#Remove o primeiro número 2 que aparecer

if 4 in num: #Se existir o número 4 na lista ele vai remover
  num.remove(4)
else:
  print('Não achei o número 4.')

print(num)
print(f'Essa lista tem {len(num)} elementos') #Ler a quantidade de elementos na lista

valores = list()

for cont in range(0, 5): #Adiciona um valor
  valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores): #Ler um valor v na posição c
  print(f'Na posição {c} encontrei o valor {v}...')
print('Cheguei ao final da lista.')

a = [2, 3, 4, 7]
b = a[:] #Cria uma cópia dos elementos de a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
