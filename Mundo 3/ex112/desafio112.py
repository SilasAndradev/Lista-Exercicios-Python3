from utilidadescev.moeda import resumo
from utilidadescev.dados import leiaDinheiro

input_Usuario = leiaDinheiro("Digite o preço: \n")

print(resumo(input_Usuario, 20, 12))