#Desafio 53  - Curso em Vídeo
#Crie um programa qualquer e diga se ela é um palíndromo desconsiderando os espaços.
frase = str(input('Digite uma frase para verificarmos se é Palíndromo: '))
frase2 = frase.lower().replace(" ", "").replace(",", "").replace(".", "")
invertido = frase2[::-1]
if frase2 == invertido:
  print('É um palindromo')
else:
  print('Não é um palindromo')
