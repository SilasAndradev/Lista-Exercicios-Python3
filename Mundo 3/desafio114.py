import urllib.request
import json

try:
    url= urllib.request.urlopen('http://pudim.com.br/')
    x= url.read()
    y = json.loads(x.decode('utf-8'))
    teste = y['valor']
    print(teste)
    
except Exception as e:
    print('O Site não está acessível no momento')
else:
    print('Consegui abrir o site com sucesso!')