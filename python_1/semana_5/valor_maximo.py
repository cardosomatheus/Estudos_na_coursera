def maximo(n1,n2,n3):
  lista_valores  = [n1,n2,n3]
  lista_valores.sort(key=int, reverse=True)

  return lista_valores[0]

if __name__ == '__main__':
  maximo(0,-2,4)