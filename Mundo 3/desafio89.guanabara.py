#Desafio 89 - Curso em Vídeo
aluno = list()
geral = list()
quant = 0

while True:
  nome = str(input('Digite o nome do aluno: '))
  aluno.append(nome)
  nota1 = float(input('Digite a primeira nota do aluno: '))
  aluno.append(nota1)
  nota2 = float(input('Digite a segunda nota do aluno: '))
  aluno.append(nota2)
  geral.append(aluno[:])
  aluno.clear()
  keep = str(input('Deseja continuar? [S/N] ')).upper().strip()
  quant += 1
  
  if keep[0] == 'N':
    break

print('-='*30)
print(f"No.  NOME {'MÉDIA':>10}")

for s in range(quant):
  nota1 = geral[s][1]
  nota2 = geral[s][2]
  v = (nota1 + nota2) / 2
  print(f"{s}    {geral[s][0]}           {v:.2f}")
  
while True:
  print('-'*30)
  s = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
  
  if s != 999:
    notas = list()
    notas.append(geral[s][1])
    notas.append(geral[s][2])
    print(f'Notas de {geral[s][0]} são: {notas}')
  else:
    break