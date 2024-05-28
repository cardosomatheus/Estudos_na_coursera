def valores_estao_ordenados():
  v1 = float(input(' valor 1: '))
  v2 = float(input(' valor 2: '))
  v3 = float(input(' valor 3: '))

  if v1 < v2 and v2 < v3:
    print('crescente') 
  else: 
    print('não está em ordem crescente')



if __name__ =='__main__':
  valores_estao_ordenados()