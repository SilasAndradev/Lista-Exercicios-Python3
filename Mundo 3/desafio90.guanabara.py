#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
aluno = dict()
aluno['nome'] = str(input('Digite o seu nome: '))
aluno['média'] = float(input('Digite a média aluno: '))
print('-='*30)
print(aluno)
print('-='*30)
print(f'O aluno {aluno["nome"]} está com {aluno["média"]} na média.')