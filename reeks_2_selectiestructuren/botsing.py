x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

x3 = int(input())
y3 = int(input())

x4 = int(input())
y4 = int(input())


linksA = min(x1,x2)
rechtsA = max(x1,x2)
onderA = min(y1,y2)
bovenA = max(y1,y2)

linksB = min(x3,x4)
rechtsB = max(x3,x4)
onderB = min(y3,y4)
bovenB = max(y3,y4)

if(rechtsA <= linksB):
    botsing = False
elif(rechtsB <= linksA):
    botsing = False
elif(bovenA <= onderB):
    botsing = False
elif(bovenB <= onderA):
    botsing = False
else:
    botsing = True


if(botsing == False):
    print("geen botsing")
else:
    print("botsing")