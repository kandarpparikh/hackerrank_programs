n = list(map(int,input().split()))
arr = list(map(int,input().split()))
bcharged = int(input())

bactual = (sum(arr)-arr[n[1]])/2
if bactual == bcharged:
    print("Bon Appetit")
else:
    print(int(bcharged-bactual))
