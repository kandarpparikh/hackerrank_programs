n= int(input())
p = int(input())
i = 1
pagecount = 0
rpagecount = 0

if n%2==1:
    if n-p<2:
        print("0")
    else:
        while i < p :
            i +=2
            pagecount += 1

        while n > p:
            n -= 2
            if n < p:
                break
            rpagecount += 1



        if pagecount > rpagecount:
            print(int(rpagecount))
        else:
            print(int(pagecount))
else:
    while i < p :
        i +=2
        pagecount += 1

    while n > p:
        n -= 2
        rpagecount += 1

    if pagecount > rpagecount:
        print(rpagecount)
    else:
        print(pagecount)
