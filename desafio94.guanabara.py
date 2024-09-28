pessoas = list()
pessoa = dict()
mulheresL = list()
médiaI = 0
idades = 0 
contI = 0
cadastroQ = 0
listaAcimaMedia = list()

while True:
    cadastroQ += 1

    pessoa['nome'] = str(input('Digite o seu nome: '))
    pessoa['sexo'] = str(input('Digite o seu sexo [M/F]: ')).upper()
    pessoa['idade'] = int(input('Digite sua idade: '))

    contI += 1
    idades += pessoa['idade']

    if pessoa['sexo'] == 'F':
        mulheresL.append(pessoa['nome'])
    
    pessoas.append(pessoa)
    pessoa.clear()
    keep = str(input('Digite se dejesa continuar: [S/N]')).upper().strip()
    
    if keep[0] == 'N':
        break

médiaI = idades / contI

print(f'Foram cadastradas {cadastroQ} pessoas.')
print(f'A média de idade do grupo é {médiaI}.')
print(f'As mulheres cadastradas foram {mulheresL}.')
print(f'As pessoas acima das médias são: ')

for dicionario in pessoas:
    if 'idade' in dicionario and dicionario['idade']  > médiaI:
        listaAcimaMedia.append(dicionario)
for dicionario in listaAcimaMedia:
    print(dicionario)
