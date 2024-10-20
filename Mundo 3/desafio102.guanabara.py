def fatorial(num, show=False):
    resultado = 1
    v = 0
    for i in range(1, num + 1):
        resultado *= i
        if show:
            if i != num:
                print(i, end=' X ')
            else:
                print(i, end=' = ')
    return resultado

numero = int(input('Digite um número: '))
result = fatorial(numero)
print(result)
