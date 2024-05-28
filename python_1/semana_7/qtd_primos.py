"""Escreva a função n_primos que recebe como argumento um número inteiro maior ou igual a 2 como parâmetro e devolve 
a quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n)."""

def e_primo(x):
    fator = 2
    valor_primo = False
    while (x % fator != 0) and (fator <= x/2):
        fator +=1 
    
    if (x % fator !=0) or (x == 2):
        valor_primo = True

    return valor_primo


def n_primos(numero):
    qtd_primos = 0
    while numero > 1:
        if e_primo(numero):
            qtd_primos +=1
        numero -=1
    return qtd_primos



