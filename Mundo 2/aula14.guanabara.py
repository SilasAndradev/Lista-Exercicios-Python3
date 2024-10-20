#Aula 14 - Curso em Vídeo
#Estrutura de repetição (while)
#For é usado quando se sabe o limite, já o While é quando não se sabe o limite
r = 'S'
par = impar = 0
while r == 'S':
  n = int(input('Digite um número: '))
  r = str(input('Quer continuar? [S/N] ')).upper()
  if n !=0:
   if n % 2 == 0:
    par += 1
   else:
    impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))