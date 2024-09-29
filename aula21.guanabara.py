# Funções (Parte 2) - Curso em Vídeo

# => Interactive Help
#   - help()

# => Docstrings

#       def contador(i, f, p):
#           """
#           -> Faz isso ou aquilo
#           """
#           c = 1
#           while c <= f:
#               print(f'{c} ', end='')
#               c += p
#           print('FIM!')
#       help(contador)

# => Argumentos opcionais

#   def somar(a, b, c=0): # Se C não receber nenhum valor ele vai valer 0
#      s = a + b+ c      # Nada impede de deixar A, B e C sendo argumentos opcionais 
#      print(s)

#   somar(3, 2, 5)
#   somar(8, 4)
#   somar()
# => Escopo de variáveis

#   def teste():
#            x = 8
#            global n1
#            n1 = 9 # Normalmente n1 é uma variavel local, mas como usei o 'global a' ele vai usar a variavel global
#            print(x) # X é uma variavel local
#            print(n) # N é uma variavel global


# Programa Principal
#   n = 2
#   n1 = 10 # n1  é uma variavel global
#   print(x)  x só funciona dentro da função teste()
#   print(n)

# => Retorno de resulutados

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 2, 5) # Return vai jogar o valor para o que vier antes
r2 = somar(5, 90)   # Nesse caso r1, r2 e r3 ]
r3 = somar(90, 89, 5476)
print(r1, r2, r3)

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    

num = int(input('Digite um número: '))
if par(num):
    print('É par')
else:
    print('Não é par')
