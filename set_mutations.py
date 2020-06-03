import math
i = input()
S = set(list(input().split()))
n = input()
x = 0
for i in range(0,int(n)):
    ops = list(input().split())
    itr_set = set(list(input().split()))
    exec("S."+str(ops[0])+"("+str(itr_set)+")")

for i in S:
    x = x + int(i)

print(x)

    rel_dic = {}
    f1 = {'1','2','3','4'}
    f2 = {'5','6','7','8'}
    for i in range(0,4):
        relation = input().split()
        rel_dic[relation[0]] = relation[1]
    print(rel_dic)

    for i in f1:
        print(rel_dic.get(i))

    for i in rel_dic:
        rel_dic.

fstlineinput = input().split()

a = []
for i in range(0,6):
    relation = input().split()
    a.append(relation)
    relation.reverse()
    a.append(relation)
    print(a)

