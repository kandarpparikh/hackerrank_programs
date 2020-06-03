def findSubstring(s, k):
    vow = ['a','e','i','o','u']
    maxcount = ['0']

    result = []
    array = []
    for i in range(len(s)-k+1):
        array.append(s[i:i+k])
    print(array)
    for x in array:
        count = 0
        for j in vow:
            if j in x:
                count += x.count(j)
        print("string {} : count {}".format(x,count) )
        if count > int(maxcount[0]):
            maxcount[0] = count
            if len(result)==0:
                result.append(x)
            else:
                result[0] = x
    print(result)
    if len(result) == 0:
        return ("Not found!")
    return (result[0])


    # Write your code here

if __name__ == '__main__':


    s = input()

    k = int(input().strip())

    result = findSubstring(s, k)
    print(result)
