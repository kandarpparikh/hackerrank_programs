n = int(input())
arr = list(input())
level = 0
counterarray = []
count = 0
result = 0
for i in arr:
    if i == "D":
        count -= 1
        counterarray.append(count)
    else:
        count += 1
        counterarray.append(count)

for i in range(1,len(counterarray)):
    if counterarray[i] == 0 and counterarray[i-1]<0:
        result += 1

print(result)
