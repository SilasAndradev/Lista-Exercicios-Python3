try:
    a = int(input('Númerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados.')
except ZeroDivisionError:
    print('Não é possível dividir por zero')
except KeyboardInterrupt:
    print('O usuário prefiriu não informar os dados')
except Exception as error:
    print(f'O erro encontrado foi {error.__class__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre.')