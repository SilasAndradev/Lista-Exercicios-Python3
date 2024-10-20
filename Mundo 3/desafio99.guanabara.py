# Exercício Python 099: Faça um programa que tenha uma 
# função chamada maior(), que receba vários parâmetros com valores inteiros. 
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(* num):

    print('-='*30)

    v = 0

    print('Analisando os valores passados...')

    while v < len(num):
        print(num[v], end=' ')
        v += 1

    print(f'Foram informados {len(num)} valores ao todo')

    pos = 0
    maior = 0

    while pos < len(num):

        if num[pos] > maior:
            maior = num[pos]

        pos +=1

    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1 )
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
