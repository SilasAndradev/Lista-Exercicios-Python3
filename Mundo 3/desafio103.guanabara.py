def ficha(nome, gols):
    if gols == '':
        gols = 0
    if (nome == ' ' or  nome == '') and gols != '':
        print(f'O jogador <desconhecido> fez {gols} gol(s) no campeonato.')
    elif (nome != ' ' or  nome != '') and gols != '':
        print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
    elif (nome == ' ' or  nome == '') and gols == '':
        print(f'O jogador <desconhecido> fez 0 gol(s) no campeonato.')
    elif (nome != ' ' or  nome != '') and gols == '':
        print(f'O jogador {nome} fez 0 gol(s) no campeonato.')

jogador = str(input('Nome do jogador: '))
num = input('Números de gols: ')
ficha(jogador, num)
