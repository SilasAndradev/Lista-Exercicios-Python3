def leiaDinheiro(input_Usuário):
    valido = False
    while not valido:
        entrada = str(input(input_Usuário)).replace(",", ".").strip()
        if entrada.isalpha() or entrada == "":
            print(f'\033[0;31mERRO: {entrada} é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)