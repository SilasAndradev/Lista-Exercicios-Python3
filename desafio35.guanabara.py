#Desafio 35 - Curso em Vídeo
#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo 
ladoA = float(input('Digite o lado A do triângulo: '))
ladoB = float(input('Digite o lado B do triângulo: '))
ladoC = float(input('Digite o lado C do triângulo: '))
if ladoA < ladoB + ladoC and ladoB < ladoA + ladoB and ladoC < ladoA + ladoB:
    print('As três retas PODEM FORMAR um triângulo.')
else:
    print('As três retas NÃO PODEM formar um triângulo.')
