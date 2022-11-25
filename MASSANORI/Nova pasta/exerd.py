from exera import test
def mistura2(a, b):
  return f'{b[0:2]+a[2:]} {a[0:2]+b[2:]}' 

test

def main():
  print ()
  print ('mistura2')
  test(mistura2('mix', 'pod'), 'pox mid')
  test(mistura2('dog', 'dinner'), 'dig donner')
  test(mistura2('gnash', 'sport'), 'spash gnort')
  test(mistura2('pezzy', 'firm'), 'fizzy perm')

if __name__ == '__main__':
  main()
