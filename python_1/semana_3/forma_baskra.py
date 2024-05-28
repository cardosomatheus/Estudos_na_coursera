import math

a = int(input('valor a:'))
b = int(input('valor b:'))
c = int(input('valor c:'))

delta = b**2 - (4*a*c)
if delta <0:
  print('esta equação não possui raízes reais')
else:
  primeira_raiz = (-b + math.sqrt(delta))/(2*a)
  segunda_raiz = (-b - math.sqrt(delta))/(2*a)
  if delta == 0:
    print(f'a raiz desta equação é {primeira_raiz}')
  else:
    if segunda_raiz < primeira_raiz:
        print(f'as raízes da equação são {segunda_raiz} e {primeira_raiz}')
    else: 
        print(f'as raízes da equação são {primeira_raiz} e {segunda_raiz}')

