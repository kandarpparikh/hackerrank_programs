from collections import OrderedDict
n = input()
#AABCAAADA
x = 2
tmp = []
for i in range(x):
    tmp = n[i*x:(i+1)*x]
    tmp = list(OrderedDict(tmp))
    print(''.join(tmp))
