sce = input()
ans_list = []
for i in range(0,int(sce)):
    setf1 = set()
    setf2 = set()
    setx = set()
    fstlineinput = input().split()
    a =[]
    for i in range(0,int(fstlineinput[1])):
        relation = input().split()
        a.append(relation)
        if '1' in relation:
            for x in relation:
                setf1.add(x)
                for n in range(len(a)):
                    if a[n][0] == x:
                        if a[n][1] not in setf1:
                            setf1.add(a[n][1])
                    elif a[n][1] == x:
                        if a[n][0] not in setf1:
                            setf1.add(a[n][0])
        elif '2' in relation:
            for y in relation:
                setf2.add(y)
                for m in range(len(a)):
                    if a[m][0] == y:
                        if a[m][1] not in setf2:
                            setf2.add(a[m][1])
                    elif a[m][1] == y:
                        if a[m][0] not in setf2:
                            setf2.add(a[m][0])
        else:
            for k in relation:
                if k in setf1:
                    for k in relation:
                        setf1.add(k)
                elif k in setf2:
                    for k in relation:
                        setf2.add(k)
                else:
                    setx.add(k)

    setf1.discard('1')
    setf1.discard('2')
    setf2.discard('1')
    setf2.discard('2')
    setf1 = setf1.difference(setf2)

    if len(list(setf1)) == 0:
        ans_list.append("-1")
    else:
        ans_list.append(sorted(list(setf1)))

for i in ans_list:
    if i == "-1":
        print("-1")
    else:
        print(" ".join(i))
