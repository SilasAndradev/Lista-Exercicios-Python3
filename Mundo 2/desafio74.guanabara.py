#Desafio 74 - Curso em Video
import random
minha_tupla = tuple(random.sample(range(10), 5))
print(minha_tupla)
tupla = sorted(minha_tupla)
print(f'O menor número é: {tupla[0]}\nO maior número é: {tupla[4]}')
