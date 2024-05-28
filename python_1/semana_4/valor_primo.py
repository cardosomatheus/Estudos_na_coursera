if __name__ == '__main__':
  valor_n = int(input('Digite o valor de n: '))
  e_primo = 0
  for i in range(1,(valor_n+1)):
    if valor_n % i == 0:
      e_primo +=1

  if e_primo > 2:
    print('não primo')
  else:
    print('primo')



    