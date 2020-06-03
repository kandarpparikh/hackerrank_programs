from itertools import combinations_with_replacement
s = input().split()

x = list(combinations_with_replacement(sorted(s[0].upper()),int(s[1])))

for i in x:
    print(''.join(i))
