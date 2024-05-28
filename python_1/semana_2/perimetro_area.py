def perimetro_e_area():        
  #Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado, calcule e imprima (saída de dados) seu perímetro e sua área.
  x = int(input(' valor correspondente ao lado de um quadrado: '))
  print(f'perímetro: {x * 4} - área: {x **2}')


if __name__ == '__main__':
  perimetro_e_area()

