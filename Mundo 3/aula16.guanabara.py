#Aula 16 - Curso em Video

#lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

#for comida in lanche:
#  print(f'Eu vou comer {comida}')

#for cont in range(0, len(lanche)):
#  print(f'Eu vou comer {lanche[cont]} na posição {cont}')

#for pos, c in enumerate(lanche):
#  print(f'Eu vou comer {c} na posição {pos}')

#print(sorted(lanche)) #Mostra a Tupla em Ordem
#print(lanche)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(4)) #Mostra quantos objetos iguais estão na Tupla
print(c.index(4)) #Mostra a posição de um item, o segundo número define a partir de qual posição deve mostrar a posição de um item

pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa) #Deleta uma variável
