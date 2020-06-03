A = set(input().split())
ans = []
x = int(input())
for _ in range(x):
    B = set(input().split())
    if B.issubset(A):
        if int(len((A.difference(B))) > 0):
            ans.append("True")
if len(ans) == x:
    print("True")
else:
    print("False")
