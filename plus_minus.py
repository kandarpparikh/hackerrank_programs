n = int(input())

arr = list(map(int, input().rstrip().split()))

zcount = 0
pcount =0
ncount =0

for i in range(len(arr)):
    if arr[i] < 0:
        ncount = ncount + 1
    elif arr[i] > 0:
        pcount = pcount + 1
    else:
        zcount = zcount + 1

print("{0:.6f}\n{1:.6f}\n{2:.6f}".format(pcount/len(arr),ncount/len(arr),zcount/len(arr)))

