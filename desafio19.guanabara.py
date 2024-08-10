#Desafio 19 - Curso em Vídeo
#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
a1 = input('Digite o nome: ')
a2 = input('Digite o nome: ')
a3 = input('Digite o nome: ')
a4 = input('Digite o nome: ')
names = [a1, a2, a3, a4]
print("A pessoa que irá apagar o quadro será:",format(random.choice(names)))
