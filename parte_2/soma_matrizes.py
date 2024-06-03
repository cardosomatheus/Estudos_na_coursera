""" Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes e devolve uma matriz que represente sua
 soma caso as matrizes tenham dimensões iguais. Caso contrário, a função deve devolver False.
"""

def soma_matrizes(matriz_1,matriz_2):
    if len(matriz_1) != len(matriz_2) or len(matriz_1[0]) != len(matriz_2[0]):
        return False
    else:
        matrizes_somada = []
        for i in range(len(matriz_1)):
            matrizes_somada.append([])
            
            for j in range(len(matriz_1[i])):
                valor = matriz_1[i][j]+matriz_2[i][j]
                matrizes_somada[i].append(valor)
    
        return matrizes_somada

    





