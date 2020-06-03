ar = list(map(int, input().rstrip().split()))
cnt =0
ar.sort()
cnt = ar.count(ar[len(ar)])
print(cnt)
