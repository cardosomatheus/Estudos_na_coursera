def fizzbuzz(n1):
  if n1 % 3 == 0 and n1 % 5 == 0:
    return 'FizzBuzz'
  elif n1 % 3 != 0 and n1 % 5 == 0:
    return 'Buzz'
  elif n1 % 3 == 0 and n1 % 5 != 0: 
    return 'Fizz'
  else:
    return n1
  


if __name__ == '__main__':
  fizzbuzz(9)
