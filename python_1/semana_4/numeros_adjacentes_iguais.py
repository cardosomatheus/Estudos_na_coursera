if __name__ == '__main__':
  n = int(input('informe um valor inteiro: '))
  antecessor = None
  e_adjacente = False
  for i in str(n):
    if antecessor is None:
      antecessor = i 
      continue
    
    if i == antecessor:
      e_adjacente = True
      break
    antecessor = i
  
  if e_adjacente:
    print('sim')
  else:
    print('não')

