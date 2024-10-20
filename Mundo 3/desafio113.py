def leiaInt(numero):
    while True:
        try:
            numero = int(input('Digite um número inteiro: '))    
        except KeyboardInterrupt:
            print('\033[0;31mO usuário prefiriu não digitar esse número.\033[m')
        except ValueError:
            print('\033[0;31mO usuário digitou um número inteiro invállido.\033[m')
        else:   
            return numero
        
def leiafloat(numero):
    while True:
        try:
            numero = float(input('Digite um número real: '))    
        except KeyboardInterrupt:
            print('\033[0;31mO usuário prefiriu não digitar esse número.\033[m')
        except ValueError:
            print('\033[0;31mO usuário digitou um número real invállido.\033[m')
        else:   
            return numero
    
inteiro = leiaInt(input)
real = leiafloat(input)

print(f'O número inteiro digitado foi: {inteiro}\nO número real digitado foi: {real}')