#!/usr/bin/env python3
import heapq
t = int(input())
for _ in range(t) :
    n = int(input())
    a_n = list(map(int,input().split()))
    if len(a_n)==2 :
        print('Yes')
        continue
    q1,q2 = [],[]
    for i in range(n) :
        if a_n[i]>0 :
            q1.append(a_n[i])
        else :
            q2.append(-a_n[i])
    if len(q2)==0 or len(q1)==0:
        qx = q2
        if len(q2)==0 :
            qx = q1
        qx.sort()
        a = qx.pop()
        b = qx.pop()
        isOK = True
        while qx :
            c = qx.pop()
            if b*b==a*c :
                a,b = b,c
                continue
            else :
                isOK = False
                break
        print('YNeos'[not(isOK)::2])
        continue
    isOK =True
    q1.sort()
    q2.sort()
    qx,qy = q1,q2
    a,b = qx[0],qy[0]
    posx,posy = 1,1
    while posx<len(qx) :
        c = qx[posx]
        # print(a,b,c,qx,qy,posx,posy,b*b==a*c)
        if b*b==a*c :
            posx += 1
            a,b = b,c
            qx,qy = qy,qx
            posx,posy = posy,posx
            continue
        isOK = False
        break
    # print(qx,qy,isOK,posx,posy)
    if isOK and posx>=len(qx) and posy>=len(qy):
        print('Yes')
        continue
    isOK =True
    qx,qy = q2,q1
    a,b = qx[0],qy[0]
    posx,posy = 1,1
    while posx<len(qx) :
        c = qx[posx]
        # print(a,b,c,qx,qy,posx,posy,b*b==a*c)
        if b*b==a*c :
            posx += 1
            a,b = b,c
            qx,qy = qy,qx
            posx,posy = posy,posx
            continue
        isOK = False
        break
    # print(qx,qy,isOK,posx,posy)
    if isOK and posx>=len(qx) and posy>=len(qy):
        print('Yes')
    else :
        print('No')
        continue
