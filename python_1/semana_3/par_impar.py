def valor_par_impar():
    valor = int(input('Digite um número inteiro: '))

    if valor % 2 == 0:
        print('par')
    else:
        print('ímpar')



if __name__ == '__main__':
    valor_par_impar()