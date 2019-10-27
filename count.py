from sys import argv
from itertools import count
startvalue = int(argv[1])
endvalue = int(argv[2])
for el in count(startvalue):
    if el > endvalue:
        break
    else:
        print(el)
