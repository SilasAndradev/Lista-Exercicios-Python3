#   Exercício Python 100: Faça um programa que tenha uma lista 
#   chamada números e duas funções chamadas sorteia() e somaPar().
#   A primeira função vai sortear 5 números e vai colocá-los dentro
#   da lista e a segunda função vai mostrar a soma entre todos os 
#   valores pares sorteados pela função anterior.

from random import randint

def sortear(lista):
    print('Sorteando 5 valores da lista:', end=' ')

    for cont in range(0, 5):

        lista.append(randint(1, 10))
        print(f'{lista[cont]}', end=' ')

    print('PRONTO!')

def somaPar(lista):
    pares = 0

    for j in lista:

        if j % 2 == 0:
            pares += j

    print(f'Somando os valores pares de {lista}, temos {pares}.')

números = list()
sortear(números)
somaPar(números)
