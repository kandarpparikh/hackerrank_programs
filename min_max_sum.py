arr = list(map(int, input().rstrip().split()))

asc = []
des = []
mx =0
mn =0
arr.sort()
for i in range(len(arr)-1):
    mx = mx + arr[i]

arr.reverse()
for i in range(len(arr)-1):
    mn = mn + arr[i]
print(str(mn)+" "+str(mx))
