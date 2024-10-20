#Desafio 73 - Curso em Video
time = ('Botafogo', 'Fortaleza', 'Palmeiras', 'Flamengo', 'Cruzeiro', 'São Paulo', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Internacional', 'Bragatino', 'Athletico-PR', 'Juventude', 'Criciúma', 'Grêmio', 'Fluminense', 'Corinthians', 'EC Vitória', 'Cuiabá', 'Atlético-GO')
print(f'Os primeiros 5 colocados são {time[0:6]}')
print(f'Os últimos colocados são {time[14: 19]}')
print('A lista em ondem fica: ''\033[0;41m'f'{sorted(time)}''\033[m')
print("O time 'Chapecoense' não está na série A")
