n = input()
result = []
for i in range(0,int(n)):
    q = list(map(int,input().split()))
    catA = q[0]
    catB = q[1]
    mouseC = q[2]

    if abs(catA-mouseC) < abs(catB-mouseC):
        result.append("Cat A")
    elif abs(catA-mouseC) > abs(catB-mouseC):
        result.append("Cat B")
    else:
        result.append("Mouse C")
for i in result:
    print(i)
