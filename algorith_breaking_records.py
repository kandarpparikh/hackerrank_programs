def breakingRecords(scores):
    lcount = []
    mcount = []
    max = scores[0]
    min = scores[0]
    res = []
    for i in scores:
        #print("-----------------------------------------")
        #print("score is :", i)
        if i > max:
            max = i
            mcount.append(1)
        if i < min:
            min = i
            lcount.append(0)
        #else:
        #    continue
        #print("mcount :",mcount)
        #print("lcount :",lcount)
    res.append(len(mcount))
    res.append(len(lcount))
    #print(res)
    return res

if __name__ == '__main__':

    n = int(input())

    scores = list(map(int, input().rstrip().split()))
    #print(scores)

    result = breakingRecords(scores)
    print(' '.join(str(x) for x in result))
