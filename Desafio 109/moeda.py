def aumentar(n, format = False):
    return n + (n * (10/100)) if format == False else moeda(n)

def diminuir(n, format = False):
    return n - (n * (10/100)) if format == False else moeda(n)

def dobro(n, format = False):
    return n * 2 if format == False else moeda(n)

def metade(n, format = False):
    return n / 2 if format == False else moeda(n)

def moeda(n, format = False):
    return f'R${n:.2f}'.replace('.',',') if format == False else moeda(n)