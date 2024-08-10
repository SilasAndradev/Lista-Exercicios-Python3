#Desafio 19 - Curso em Vídeo
#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
names = ["Silas", "Yulo", "Oséias", "Pedro"]
print("A pessoa que irá apagar o quadro será:",format(random.choice(names)))
