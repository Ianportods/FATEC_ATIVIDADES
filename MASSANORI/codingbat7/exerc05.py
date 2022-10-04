from exer02 import test
def hello_name(name):
  return (f'Hello {name}!')

test

def main():
    print()
    print('Hello Name')
    test(hello_name('Bob'), 'Hello Bob!')
    test(hello_name('Alice'), 'Hello Alice!')
    test(hello_name('X'), 'Hello X!')
    test(hello_name('Hello'), 'Hello Hello!')
if __name__ == '__main__':
        main()