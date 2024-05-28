if __name__ == '__main__':
  n = int(input('Digite o valor de n: '))
  if n == 0:
    fatorial = 1
  else:
    fatorial = n
    for i in range(n,1,-1):
      fatorial = fatorial * (i-1)

  print(fatorial) 