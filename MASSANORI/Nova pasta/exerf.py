from exera import test
def busca(frase, palavra):
  return len([k for k in range(len(frase)) if frase[k:k+len(palavra)] == palavra])

test

def main():
  print ()
  print ('busca')
  test(busca('ana e mariana gostam de banana', 'ana'), 4)
  test(busca('uma arara ou duas araras', 'ara'), 4)

if __name__ == '__main__':
  main()