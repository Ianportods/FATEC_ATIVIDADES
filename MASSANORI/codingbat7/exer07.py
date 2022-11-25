from exer02 import test
def extra_end(s):
  return 3 * s[-2:]

test

def main():
  print()
  print('Extra End')
  test(extra_end('Hello'), 'lololo')
  test(extra_end('ab'), 'ababab')
  test(extra_end('Hi'), 'HiHiHi')
  test(extra_end('Candy'), 'dydydy')
  test(extra_end('Code'), 'dedede')
if __name__ == '__main__':
    main()