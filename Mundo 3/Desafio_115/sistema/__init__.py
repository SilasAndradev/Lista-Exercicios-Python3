def sistema():
    while True:
        print('-'*40)
        print(f"{'MENU PRINCIPAL':^40}")
        print('-'*40)
        print('\033[0;33m1 - \033[m\033[0;34mVer pessoas cadastradas')
        print('\033[0;33m1 - \033[m\033[0;34mCadastrar nova pessoa')
        print('\033[0;33m1 - \033[m\033[0;34mSair do sistema')
        print('-'*40)
        resposta = int(input('\033[0;33mSua Opção: \033[m'))
        print('-'*40) 
        if resposta == 1:
            print('-'*40)
            print(f"{'PESSOAS CADASTRADAS':^40}")
            print('-'*40)
            arquivo = open("texto.txt", "r")
            conteudo = arquivo.read()
            print(conteudo)
        elif resposta == 2:
            print('-'*40)
            print(f"{'NOVO CADASTRO':^40}")
            print('-'*40)
            arquivo = open('novo_texto.txt', 'w')
            nome = str(input('NOME:'))
            arquivo.write(nome)
            arquivo.write(int(input('IDADE:')))
            print(f'Novo resgistro de {nome} adicionado.')
            arquivo.close()
        elif resposta == 3:
            print('-'*40)
            print(f"{'Saindo do sistema... Até logo!':^40}")
            print('-'*40)
            break
        else:
            print(f'\033[0;31mERRO: Digite uma opção válida!\033[m')

    return 0


            
        