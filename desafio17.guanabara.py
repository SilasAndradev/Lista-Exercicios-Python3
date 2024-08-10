#Desafio 17 - Curso em Vídeo
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retâgulo, calcule e mostre o comprimento da hipotenusa
import math
num = float(input('Digite o valor do primeiro Cateto'))
num2 = float(input('Digite o valor do segundo Cateto'))
#1° Forma
print(math.hypot(num, num2))
#2° Forma
print(math.sqrt(num*num + num2*num2))
