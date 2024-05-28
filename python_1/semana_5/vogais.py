def vogal(letra):
    e_vogal = False
    letra = letra.upper().strip()
    lista_vogal = ['A','E','I','O','U']
    if letra in lista_vogal:
      e_vogal =True

    return e_vogal


if __name__ == '__main__':
   vogal('a')
   vogal(' i    ')
   vogal('e')
   vogal('j')