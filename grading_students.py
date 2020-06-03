n = int(input())
arr = []
for i in range(0,n):
    ele = int(input())
    arr.append(ele)
x =0
tmp =0
for i in range(len(arr)):
    if arr[i] >= 38:
        if arr[i]%5 == 0:
            continue
        else:
            x = (int(arr[i]/5) + 1)*5
            if x - arr[i] < 3:
                arr[i] = x
            else:
                continue
    else:
        continue
for i in range(len(arr)):
    print(arr[i])
