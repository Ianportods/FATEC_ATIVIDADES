from exera import test
def palindrome(s):
  if s[::-1] == s:
      return True
  else:
      return False

test

def main():
  print ()
  print ('palindrome')
  test(palindrome('asa'), True)
  test(palindrome('casa'), False)

if __name__ == '__main__':
  main()