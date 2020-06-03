resultarr = [0]*int(input())
arr = input().split()

for i in arr:
    resultarr[int(i)] += 1
print(resultarr.index(max(resultarr)))
