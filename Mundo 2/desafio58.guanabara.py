#Desafio 58 - Curso em Video
#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random
c = 0
while c < 1:
  num = random.randint(0, 10)
  res = int(input('Digite o número que você achar que o computador acertou: '))
  if res == num:
    print('Parabéns!! Você acertou :)')
    c += 1
  else:
    print('Você errou.')
