#Desafio 56  - Curso em Vídeo
#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo.
# - Qual é o nome do homem mais velho.
# - Quantas mulheres tem menos de 20 anos.
somaIdades = 0
maiorIdade = 0
nomeHomemVelho = ('Não tem ninguém.')
mulheresNovas = 0
for c in range(1, 5):
  nome = str(input('Digite seu nome: '))
  sexo = int(input('Digite seu sexo, 1 para Masculino e 2 para Feminino: '))
  idade = int(input('Digite sua idade: '))
  somaIdades = somaIdades + idade
  if c == 1:
    maiorIdade = idade
  if maiorIdade < idade and sexo == 1:
    maiorIdade = idade
    nomeHomemVelho = nome
  if idade < 20 and sexo == 2:
    mulheresNovas = mulheresNovas + 1
print('A média das idade é {}, o nome do homem mais velho é {} e tem {} mulheres com menos de 20 anos.'.format(somaIdades / 4, nomeHomemVelho, mulheresNovas))
