n = int(input())
arr = input().split()
colors = set(arr)
result = []
for i in colors:
    result.append(int(arr.count(i)/2))
#    print("color {} -> count {} -> pairs {}".format(i,arr.count(i),int(arr.count(i)/2)))
print(sum(result))
