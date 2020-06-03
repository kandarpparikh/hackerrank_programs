def dynamicArray(n, queries):
    s1 = []
    s0 = []
    lastanswer = [0]
    for k in range(len(queries)):
        #print("query is ",queries[k])
        if queries[k][0] == 1:
            if (((queries[k][1] ^ lastanswer[-1])%n) == 0):
                s0.append(queries[k][2])
            else:
                s1.append(queries[k][2])
        else:
            if (((queries[k][1] ^ lastanswer[-1])%n) == 0):
                lastanswer.append(queries[i][1]%len(s0))
            else:
                lastanswer.append(s1[0])
        #print("array of s0 : ", s0)
        #print("array of s1 :", s1)
        #print("lastanswer : ", lastanswer)
        #print("------------------------------------------")
    lastanswer.remove(lastanswer[0])
    return lastanswer
    # Write your code here

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    for i in result:
        print(i)
