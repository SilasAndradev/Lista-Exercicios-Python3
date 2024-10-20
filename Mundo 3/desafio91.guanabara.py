import random

num = 1
jogadores = dict()

jogadores['jogador1'] = random.randint(1, 6)
print(f'O jogador1 tirou {jogadores["jogador1"]}')
jogadores['jogador2'] = random.randint(1, 6)
print(f'O jogador2 tirou {jogadores["jogador2"]}')
jogadores['jogador3'] = random.randint(1, 6)
print(f'O jogador3 tirou {jogadores["jogador3"]}')
jogadores['jogador4'] = random.randint(1, 6)
print(f'O jogador4 tirou {jogadores["jogador4"]}')

print('-='*30)

for item in sorted(jogadores, key = jogadores.get):
    print(f'{num}° lugar: {jogadores[item]}')
    num += 1

print('-='*30)