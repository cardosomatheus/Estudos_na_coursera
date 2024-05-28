def fatura_cliente_por_email():
  Nome = str(input('Digite o nome do Nome:')).title()
  Dia  = str(input('Digite o Dia de vencimento:'))
  Mês  = str(input('Digite o Mês de vencimento:')).title()
  Valor = str(input('Digite o valor da fatura:'))
  print(f'Olá, {Nome}\nA sua fatura com vencimento em {Dia} de {Mês} no valor de R$ {Valor} está fechada.')


if __name__ == '__main__':
  fatura_cliente_por_email()