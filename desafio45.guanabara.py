#Desafio 45  - Curso em Vídeo
#Crie um programa que faça o computador jogar Jokenpô com você
import random
maoComputador = random.choice(['Pedra','Papel','Tesoura'])
maoUsuario = str(input("Escolha:\nPedra\nPapel\nTesoura\n"))
print('O computador escolheu: {}'.format(maoComputador))
print('O você escolheu: {}'.format(maoUsuario))
if maoComputador == maoUsuario:
  print('Empate')
elif (maoComputador == 'Pedra' and maoUsuario == 'Papel') or (maoComputador == 'Papel' and maoUsuario == 'Tesoura') or (maoComputador == 'Tesoura' and maoUsuario == 'Pedra'):
  print('Você ganhou.')
elif (maoComputador == 'Papel' and maoUsuario == 'Pedra') or (maoComputador == 'Tesoura' and maoUsuario == 'Papel') or (maoComputador == 'Pedra' and maoUsuario == 'Tesoura'):
  print('Você perdeu.')
else:
  print('Você digitou errado :)')
