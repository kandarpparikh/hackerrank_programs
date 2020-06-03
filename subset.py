ans = []
for _ in range(int(input())):
    n = input()
    A = set(input().split())
    x = input()
    B = set(input().split())
    ans.append(bool(len(A.difference(B)) == 0))
for i in ans:
    print(i)
