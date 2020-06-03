n = int(input())
arr1 = list(map(int,input().split()))

n = int(input())
arr2 = list(map(int,input().split()))

s1 = set(arr1)
s2 = set(arr2)

x = sorted(list(set(list(s1.difference(s2)) + list(s2.difference(s1)))))

print(x)

#for i in range(len(x)):
#    print(x[i])
