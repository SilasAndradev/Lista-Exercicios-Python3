#Desafio 88 - Curso em Vídeo
from random import randint
jogo = list()
plap = list()

print('-'*30)
print(f"{'JOGO DA MEGA SENA':^30}")
print('-'*30)

jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f"-=-=-= SORTEANDO {jogos} JOGOS -=-=-=")

for j in range(1, jogos+1):
  
  for i in range(0, 6):
    num = randint(1, 60)
    
    while num in plap:
      num = randint(1, 60)
    
    plap.append(num)
  
  jogo.append(plap[:])
  plap.clear()

for c in range(jogos):
  print(f'Jogo {c+1}: {sorted(jogo[c])}')

print('-='*5, 'BOA SORTE', '=-'*5)