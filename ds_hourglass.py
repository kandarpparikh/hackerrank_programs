arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))
farray = []
print(arr)
# 1st ow upto 3 , 2nd row 2nd element , 3rd row 1st 3 elements

for i in range(0,4):
    sum = 0
    for j in range(0,4):
        sum = sum + arr[i][j] + arr[i][j+1]+ arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1]+ arr[i+2][j+2]
        farray.append(sum)
        sum = 0


