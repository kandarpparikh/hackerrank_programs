
import itertools
from itertools import permutations
s = input().split()
x = list(permutations(s[0].upper(),int(s[1])))
for i in x:
    print(''.join(i))
