def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(len(ar)):
        for j in range(1+i,len(ar)):
            if ar[j] > ar[i] and (ar[j]+ar[i])%k == 0:
                count = count + 1
    return count

if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)
    print(result)
