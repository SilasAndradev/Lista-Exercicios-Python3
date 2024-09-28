jogador = dict()
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gol = list()
tol = 0
tol3 = 0

for j in range(1, partidas+1):
    tol = int(input(f'Quantos gols na partida {j}?'))
    gol.append(tol)
    tol3 += tol

jogador['gols'] = gol.copy()
jogador['total'] = tol3

print('-='*30)
print(jogador)
print('-='*30)
print(f'O campo nome tem o valor {jogador["nome"]}.')
print(f'O campo gols tem o valor {jogador["gols"]}.')
print(f'O campo total tem o valor {jogador["total"]}.')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')

for k in range(1, partidas+1):
    print(f'    => Na partida {k}, fez {gol[k-1]}')
print(f'Foi um total de {tol3} gols')
