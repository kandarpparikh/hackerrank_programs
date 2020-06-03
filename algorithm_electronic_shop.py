n= list(map(int,input().split()))
keyboard = list(map(int,input().split()))
usb = list(map(int,input().split()))
total = []
mx = -1
for i in keyboard:
    for j in usb:
        if (i+j)<=n[0] and (i+j)>mx:
            mx = (i+j)



if mx == -1:
    print("-1")
else:
    print(mx)
