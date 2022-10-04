
def multstring(s, n):
    a = (s*n)
    return a


def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('Multstring')
  test(multstring('Hi', 2), 'HiHi')
  test(multstring('Hi', 3), 'HiHiHi')
  test(multstring('Hi', 1), 'Hi')
  test(multstring('Hi', 0), '')
  test(multstring('Hi', 5), 'HiHiHiHiHi')
  test(multstring('Oh Boy!', 2), 'Oh Boy!Oh Boy!')
  test(multstring('x', 4), 'xxxx')
  test(multstring('', 4), '')
  test(multstring('code', 2), 'codecode')
  test(multstring('code', 3), 'codecodecode')

  if __name__ == '__main__':
      main()