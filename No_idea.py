import itertools

inputlist = list(map(int, input().split()))
arr = list(map(int, input().split()))
A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))

hcount =0
scount =0

for i in arr:
    if i in A:
        hcount = hcount +1
    if i in B:
        scount = scount + 1
    else:
        continue

#hcount = list(arr.intersection(A))
#scount = list(arr.intersection(B))

#sum = len(hcount - len(scount)
print(hcount-scount)
