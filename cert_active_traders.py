def mostActive(customers):
    array = []
    e = len(customers)*0.05
    s = list(set(customers))
    for x in range(len(customers)):
        tmp =x
        count = 0
        if x == tmp:
            count += 1
        if count >= e:
            if x not in array:
                array.append(x)
    #for x in s:
    #    if customers.count(x) >= len(customers)*0.05:
    #        array.append(x)
    #print(array)
    return (sorted(array))

    # Write your code here

if __name__ == '__main__':

    customers_count = int(input().strip())

    customers = []

    for _ in range(customers_count):
        customers_item = input()
        customers.append(customers_item)

    result = mostActive(customers)

    for i in range(len(result)):
        print(result[i])

