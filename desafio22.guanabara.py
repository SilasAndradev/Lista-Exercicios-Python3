#Desaio 22 - Curso em Vídeo
#Crie um programa que leia o nome complpeto de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúsculas
#Quantas letras ao todo(sem considerar os espaços).
#Quantas letras tem o primeiro nome

nomeCompleto = input('Digite o seu nome completo: ')
nome = nomeCompleto.split()
nomeCompleto2 = nomeCompleto.replace(" ", "")

print('O seu nome todo maiúsculo seria {}.'.format(nomeCompleto.upper()))
print('O seu nome todo minúsculo seria {}.'.format(nomeCompleto.lower()))
print('A quantidade de caractéres do seu nome (sem espaços) é: {}'.format(len(nomeCompleto2)))
print('O seu primeiro nome tem {} letras.'.format(len(nome[0])))
