from exera import test
def fixa_primeiro(s):
  b = s[0]
  c = s[1:]
  return b + c.replace(b, '*')

test

def main():
  print ()
  print ('fixa_primeiro')
  test(fixa_primeiro('babble'), 'ba**le')
  test(fixa_primeiro('aardvark'), 'a*rdv*rk')
  test(fixa_primeiro('google'), 'goo*le')
  test(fixa_primeiro('donut'), 'donut')

if __name__ == '__main__':
  main()
