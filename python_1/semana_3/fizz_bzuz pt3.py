def fizbuzz3():
    valor = int(input('Digite um número inteiro: '))

    if valor % 3 == 0 and valor % 5 == 0:
      print('FizzBuzz')
    else:
      print(valor)  



if __name__ == '__main__':
    fizbuzz3()