from uteis import números

num = int(input("Digite um valor: "))

fat = números.fatorial(num)
triplo = números.triplo(num)
dobro = números.dobro(num)

print(f'O fatorial de {num} é {fat} :)')
print(f'O fatorial de {num} é {triplo}')
print(f'O fatorial de {num} é {dobro}')