def maior_primo(n1):
  if n1 > 1:
    for i in range(n1,0,-1):     
      if e_primo(i):
        return i
        break

def e_primo(valor_do_loop):
  bool_primo = True
  e_primo = 0
  for i in range(1,(valor_do_loop+1)):
    if valor_do_loop % i == 0:
      e_primo +=1

  if e_primo > 2:
    bool_primo = False
  return bool_primo

if __name__ =='__main__':
    maior_primo(10)
    maior_primo(100)
    maior_primo(7)
    maior_primo(20)