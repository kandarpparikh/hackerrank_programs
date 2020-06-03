def countApplesAndOranges(s, t, a, b, apples, oranges):
    acount =0
    ocount =0
    for i in apples:
        if s<= i+a <=t:
            acount = acount +1
    for i in oranges:
        if s<= i+b <=t:
            ocount = ocount +1
    print(str(acount)+"\n"+str(ocount))




if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
