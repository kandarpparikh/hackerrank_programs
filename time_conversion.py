import math
s = input()

#07:05:45PM
x = 0
if s[len(s)-2:] == 'PM':
    if s[:2] == '12':
        news = s[:len(s)-2]
    else:
        x = int(s[:2]) + 12
        news = str(x) + s[2:len(s)-2]
elif s[len(s)-2:] == 'AM':
    if s[:2] == '12':
        news = "00" + s[2:len(s)-2]
    else:
        news = s[:len(s)-2]

print (news)


#12:00:00PM
