from itertools import count


meuArquivo = open('def.txt', 'r')
a = meuArquivo.readlines()
print (a.count('\n'))

