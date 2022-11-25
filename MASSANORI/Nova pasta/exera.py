def donuts(n):
  if n < 10:
      return f'Número de donuts: {n}'
  else:
      return f'Número de donuts: muitos'
  
def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('donuts')
  test(donuts(4), 'Número de donuts: 4')
  test(donuts(9), 'Número de donuts: 9')
  test(donuts(10), 'Número de donuts: muitos')
  test(donuts(99), 'Número de donuts: muitos')

if __name__ == '__main__':
  main()