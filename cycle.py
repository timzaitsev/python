from sys import argv
from itertools import cycle
endvalue = int(argv[1])
list = [un for un in argv[2]]
i = 0
for el in cycle(list):
    if i > endvalue:
        break
    print(el)
    i +=1
