def valor_da_dezena():
    valor = int(input('Digite um número inteiro: '))

    if valor < 10:
        print(f'O dígito das dezenas é 0')
    else:
        valor = int(str(valor)[-2])
        print(f'O dígito das dezenas é {valor}')



if __name__ == '__main__':
    valor_da_dezena()