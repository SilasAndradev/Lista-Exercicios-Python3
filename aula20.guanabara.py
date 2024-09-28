# Aula 20 - Curso em Vídeo
# Funções (Parte 1)

def mostraLinha():
    print('-='*30)

def mensagem(msg):
    mostraLinha()
    print(msg)
    mostraLinha()

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(s)
    print(f'A soma A + B = {s}')
    
def contador(* núm):
    tam = len(núm)
    print(f'Recebi os valore {núm} e são ao todo {tam} números')

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*=2
        pos +=1

def outraSoma(* valor):
    p = 0
    for v in valor:
        p += v
    print(f'Somando os valores {valor} temos {p}')


# Programa principal
mensagem(str(input('Digite algo: ')))

soma(4, 5)

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

valores = [2, 9, 90, 78]

dobra(valores)

print(valores)

outraSoma(5, 2)
outraSoma(2, 9, 4)
