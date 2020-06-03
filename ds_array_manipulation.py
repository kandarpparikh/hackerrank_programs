nm = input().split()

n = int(nm[0])

m = int(nm[1])

queries = []

for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))
a=[0]*(n)
#print("initial array :",a)

for i in range(len(queries)):
 #   a[queries[i][1]] = a[queries[i][1]] + queries[i][2]
 #   a[queries[i][1]] = a[queries[i][1]] + queries[i][2]

    for j in range(queries[i][0]-1,queries[i][1]):
        a[j] = a[j] + queries[i][2]
    #print("array after"+str(i)+"th iteration : ",a)
print(max(a))
