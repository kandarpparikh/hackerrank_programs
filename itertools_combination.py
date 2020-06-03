from itertools import combinations
s = input().split()
#print(list(combinations(sorted(s[0].upper()),int(s[1])-1)))
#print((slice(s[0].upper())))
#for i in x:
#    print(''.join(i))
for i in range(int(s[1])):
    y = list(combinations(sorted(s[0].upper()),i+1))
    for i in y:
        print(''.join(i))
