#Aula 12 - Curso em Vídeo
#Condições Aninhadas
nome = str(input('Digite seu nome: '))
if nome == 'Gustavo':
  print('Que nome bonito')
elif nome == 'Pedro' or nome =='Paulo':
  print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
  print('Belo nome feminino')
else:
  print('Seu nome é bem normal.')
print('Tenha um bom dia, {}'.format(nome))
