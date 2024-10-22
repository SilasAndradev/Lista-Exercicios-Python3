def sistema():
    while True:
        try:
            
            print('-'*40)
            print(f"{'MENU PRINCIPAL':^40}")
            print('-'*40)
            print('\033[0;33m1 - \033[m\033[0;34mVer pessoas cadastradas')
            print('\033[0;33m1 - \033[m\033[0;34mCadastrar nova pessoa')
            print('\033[0;33m1 - \033[m\033[0;34mSair do sistema')
            print('-'*40)
            resposta = int(input('\033[0;33mSua Opção: \033[m'))
            print('-'*40) 
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO: {resposta} o número digitado não é um inteiro\033[m')
        except 
            print(f'\033[0;31mERRO: {resposta} o número digitado não é um inteiro\033[m')