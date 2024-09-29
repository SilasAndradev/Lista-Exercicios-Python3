from datetime import date

def voto(num):
    anoHJ = date.today().year
    idade = anoHJ - num
    if idade < 16:
        print(f'Com {idade} anos: VOTO NEGADO')
    elif idade >= 16 and idade < 18:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    elif 18 <= idade < 65:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')
    else:
        print(f'Com {idade} anos: VOTO OPCIONAL')


numero = int(input('em que ano você nasceu? '))
voto(numero)
