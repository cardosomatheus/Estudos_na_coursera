# Escreva uma função dimensoes(matriz) que recebe uma matriz como parâmetro e imprime as 
# dimensões da matriz recebida, no formato iXj.

def dimensoes(matriz):
    altura = str(len(matriz))
    lagura = str(len(matriz[0]))

    print(altura+'X'+lagura)

