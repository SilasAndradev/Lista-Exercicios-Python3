# Aprimore o desafio 93 para que ele funcione com vários 
# jogadores, incluindo um sistema de visualização de detalhes do 
# aproveitamento de cada jogador.
jogadores = list()

while True:

    jogador = dict()  
    gol = list()      
    tol3 = 0          

    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for j in range(1, partidas+1):

        tol = int(input(f'Quantos gols na partida {j}? '))
        gol.append(tol)
        tol3 += tol

    jogador['gols'] = gol.copy()
    jogador['total'] = tol3
    jogadores.append(jogador.copy())

    resp = str(input('Quer continuar [S/N]: ')).upper().strip()
    if resp == 'N':
        break

print('-='*30)

print(f'cod Nome        gols            Total')

for z in range(0, len(jogadores)):

    print(f'{z} {jogadores[z]["nome"]}      {jogadores[z]["gols"]}          {jogadores[z]["total"]}')

print('-='*30)
while True:

    x = int(input('Mostrar dados de qual jogador? (999 para sair) '))
    
    if x == 999:
        print('Encerrando a visualização de dados.')
        break

    if x >= len(jogadores) or x < 0:
        print(f'Erro! Não existe jogador com código {x}. Tente novamente.')
    else:
        print(f'Levantamento do jogador {jogadores[x]["nome"]}:')
        
        for i, g in enumerate(jogadores[x]['gols']):
            print(f'   => No jogo {i+1}, ele fez {g} gol(s).')

    print('-='*30)
