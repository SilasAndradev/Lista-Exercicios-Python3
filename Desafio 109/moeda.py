def aumentar(n, format = False):
    res = n + (n * (10/100)) 
    return res if format == False else moeda(res)

def diminuir(n, format = False):
    res = n - (n * (10/100))
    return res if format == False else moeda(res)

def dobro(n, format = False):
    res = n * 2 
    return res if format == False else moeda(res)

def metade(n, format = False):
    res = n / 2
    return res if format == False else moeda(res)

def moeda(n):
    return f'R${n:.2f}'.replace('.',',')