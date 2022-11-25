from exera import test
def pontas(s):
  if len(s) <= 2:
      return f''
  else:
      return s[0:2] + s[-2:]

test

def main():
  print ()
  print ('pontas')
  test(pontas('palmeiras'), 'paas')
  test(pontas('algoritmos'), 'alos')
  test(pontas('a'), '')
  test(pontas('xyz'), 'xyyz')

if __name__ == '__main__':
  main()