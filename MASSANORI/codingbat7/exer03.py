from exer02 import test
def array_count9(nums):
  return nums.count(9)

test

def main():
    print ()
    print ('Array count 9')
    test(array_count9([1, 99, 9]), 1)
    test(array_count9([1, 9, 9]), 2)
    test(array_count9([1, 9, 9, 3, 9]), 3)
    test(array_count9([1, 2, 3]), 0)
    test(array_count9([]), 0)
    test(array_count9([4, 2, 4, 3, 1]), 0)
    test(array_count9([9, 2, 99, 3, 1]), 1)
if __name__ == '__main__':
        main()
