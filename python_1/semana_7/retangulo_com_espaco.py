"""Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes à largura e à altura 
de um retângulo, respectivamente. O programa deve imprimir, usando repetições encaixadas (laços aninhados), uma cadeia de caracteres
 que represente o retângulo informado com caracteres '#' na saída, mas de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.."""

largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))

alt = 0
while alt < altura:
    larg = 0
    qtd_asteristico = ''
    while larg < largura:
        if alt > 0 and alt < (altura-1):
            if larg in (0,(largura-1)): 
                qtd_asteristico += '#'
            else:
                qtd_asteristico += ' '
        else:
            qtd_asteristico += '#'
        larg += 1
    print(qtd_asteristico)
    alt += 1
