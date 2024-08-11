#Aula 9 - Manipulando Texto - Curso em Vídeo

frase = 'Curso em vídeo Python'
print(frase[0:15:3])
#primeiro número = onde começa 
#segudno número = onde termina
#terceiro número = quantas letras pula

print(frase.count('o',0,13))
#Conta quantos 'o' tem na frase do 0 ao 13

print(len(frase))
#conta as quantidades de caracteres

print(frase.find('deo'))
#Ele fala onde está 'deo'

print(frase.find('Android'))
#Se algo não existe na string ele retorna -1

print('Curso' in frase)
#Se algo existe na frase ele vai dizer True

print(frase.replace('Python', 'Android'))
#Troca o que tá na frase, mas tem de forma secundária

print(frase.upper())
#Ele colocar tudo em MAIÚSCULO

print(frase.lower())
#Faz justamente o contrário do anterior

print(frase.capitalize())
#Tudo fica minúsculo menos a primeira letra

print(frase.title())
#Ele faz o capitalaze, mas em cada palavra

frase2 = '  Aprenda Python  '
print(frase2.strip())
#Remove os espaços inúteis

print(frase2.rstrip())
#Ele remove apenas os espaços inúteis da direita

print(frase2.lstrip())
#Ele remove apenas os espaços inúteis da esquerda

print(frase.split())
#Ele divide a frase em palavras

print('-'.join(frase))
#Ele coloca traços :)

frase = frase.replace('Python', 'Ándroid')
print(frase)
print(frase.lower().find('vídeo'))
dividido = frase.split()
print(dividido[2][3])
