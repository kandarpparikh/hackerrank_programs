i = input()
e = list(input().split())
i = input()
f = list(input().split())
E = set()
F = set()
for i in e:
    E.add(i)
for i in f:
    F.add(i)
#print(len(E.union(F)))
#print(len(E.intersection(F)))
#print(len(F.difference(E)))
F = {1,2,3,4,5}
E = {1,2,3,4,5}
F = F.difference(E)
print(list(F))

