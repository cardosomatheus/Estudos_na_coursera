import math

if __name__ == '__main__':
      
  px1 = int(input(' valor 1: '))
  py1 = int(input(' valor 2: '))
  px2 = int(input(' valor 3: '))
  py2 = int(input(' valor 4: '))

  valor_calculo = ((px1 - px2)**2) + ((py1 - py2)**2)
  distancia = math.sqrt(valor_calculo)
  if distancia >= 10:
    print('longe')
  else:
    print('perto')
