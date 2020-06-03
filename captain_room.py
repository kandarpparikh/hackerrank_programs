i = input()
n = list(map(int,input().split()))
a = list(n)

single = set()
multiple = set()
for i in a:
    if i in single:
        multiple.add(i)
    else:
        single.add(i)
print(single)
print(multiple)
print(single.difference(multiple).pop())

