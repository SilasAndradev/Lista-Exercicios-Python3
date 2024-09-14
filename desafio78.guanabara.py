#Desafio 17 - Curso em Video
valor = list()
for i in range(0, 5):
  valor.append(int(input('Digite um valor: ')))
maior = max(valor)
menor = min(valor)
posicaoMaior = [i for i, v in enumerate(valor) if v == maior]
posicaoMenor = [i for i, v in enumerate(valor) if v == menor]
print(f'O maior valor digitado foi {maior} na posição {posicaoMaior}')
print(f'O menor valor digitado foi {menor} na posição {posicaoMenor}')
