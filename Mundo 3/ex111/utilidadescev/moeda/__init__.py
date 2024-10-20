def aumentar(n= 0, taxa = 0, format = False):
    res = n + (n * (taxa/100)) 
    return res if format is False else moeda(res)

def diminuir(n = 0, taxa = 0, format = False):
    res = n - (n * (taxa/100))
    return res if format is False else moeda(res)

def dobro(n = 0, format = False):
    res = n * 2 
    return res if not format else moeda(res)

def metade(n = 0, format = False):
    res = n / 2
    return res if not format else moeda(res)

def moeda(n):
    return f'R${n:>.2f}'.replace('.',',')

def resumo(n, aumento, redução):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço Analisado: \t{moeda(n)}')
    print(f'Dobro do Preço: \t{dobro(n, True)}')
    print(f'Metade do Preço: \t{metade(n, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(n, aumento, True)}')
    print(f'{redução}% de redução: \t{diminuir(n, redução, True)}')
    print('-'*30)