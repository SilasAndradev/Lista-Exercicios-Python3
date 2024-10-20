from time import sleep

def contador(ini, fim, passo):
    if passo < 0:
        passo *= -1
    
    if passo == 0:
        passo = 1
    print('-='*20)
    print(f'Contagem de {ini} até {fim} de {passo} em {passo}.')
    sleep(2.5)

    if ini < fim:

        cont = ini

        while cont <= fim:
            print(f'{cont}', end=', ', flush=True)
            sleep(0.5)
            cont += passo
        print('FIM')
    
    else:

        cont = ini

        while cont >= fim:
            print(f'{cont}', end=', ', flush=True)
            sleep(0.5)
            cont -= passo
        print('FIM')

contador(1, 10, 1)
contador(10, 0, 2)

print('-='*20)
print('Agora é sua vez de personalizar a contagem.')

inicio = int(input('Início: '))
final = int(input('Final:   '))
passos = int(input('Passo:  '))

contador(inicio, final, passos)
