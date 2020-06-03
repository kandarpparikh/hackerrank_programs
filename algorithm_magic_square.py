s = []

for _ in range(3):
    s.append(list(map(int, input().split())))

print(s)
ms = []
for i in range(1,9):
    for j in range(1,9):
        for k in range(1,9):
            ms[i][j] = k
