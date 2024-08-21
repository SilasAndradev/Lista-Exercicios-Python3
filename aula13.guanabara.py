#Aula 13  - Curso em Vídeo
for a in range(6, 0, -1): #Conta para trás
  print(a)
for b in range(0, 100): #Conta de 0 a 99
  print(b)
for d in range(0, 7, 2): #Conta de 0 a 6 pulando de 2 em 2
  print(d)
n = int(input('Digite um número: ')) 
for e in range(0, n+1): #Conta de 0 até N + 1
  print(e)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for v in range(i, f+1, p):
  print(v)
p = 0
for z in range(0, 3): #Cria um laço para uma somatória
  l = int(input('Digite um número: '))
  p += l
print('O somatório de todos os valores foi {}'.format(p))
