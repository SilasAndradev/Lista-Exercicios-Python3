# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) 
# em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de 
# contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date

dataHJ = date.today().year
print(dataHJ)

pessoa = dict()
pessoa['nome'] = str(input('Digite seu nome: '))
pessoa['ano de nascimento'] = v = int(input('Digite em que ano você nasceu: '))
pessoa['idade'] = dataHJ - v
pessoa['cpts'] = int(input('Digite sua CPTS: '))

if pessoa['cpts'] != 0:
    pessoa['ano de contratação'] = int(input('Digite o ano em que você foi contratado: '))
    pessoa['salário'] = int(input('Digite o seu salário: '))
    pessoa['aposentadoria'] = (pessoa['ano de contratação'] - pessoa['ano de nascimento']) + 35

print('-='*30)
print(f'{pessoa["nome"]} nasceu em {pessoa["ano de nascimento"]}, tem {pessoa["idade"]}')

if pessoa['cpts'] != 0:
    print(f'{pessoa["nome"]} ganha {pessoa["salário"]} por mês, foi contratado em {pessoa["ano de contratação"]} e vai se aposentar em {pessoa["aposentadoria"]}')