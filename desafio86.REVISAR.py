#Desafio 86 - Curso em Vídeo
pessoas = list()
dado = list()
maior = 0
menor = 6000
maiorList = list()
menorList = list()
while True:
  
  dado.append(str(input('Digite seu nome: ')))
  dado.append(int(input('Digite seu peso: ')))
  
  if dado[1] > maior:
    maior = dado[1]

  if dado[1] < menor:
    menor = dado[1]

  for p in pessoas:
    if p[1] == maior:
      maiorList.append(p[0])
    elif p[1] == menor:
      menorList.append(p[0])
  
  pessoas.append(dado[:])
  
  dado.clear()
  
  keep = str(input('Quer continuar? [S/N] ')).upper().strip()
  if keep[0] == 'N':
    break



print('-='*40)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi {maior}. Peso de {maiorList}')
print(f'O maior peso foi {menor}. Peso de {menorList}')
