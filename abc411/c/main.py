#!/usr/bin/env python3
n,q = map(int,input().split())
a_q = list(map(int,input().split()))
masu = [0]*n
ans = 0
for a in a_q :
    masu[a-1] = 1-masu[a-1]
    # print(masu)
    if n == 1 :
        print(masu[a-1])
        continue
    if (a==1 and masu[0:2]==[1,0]) \
    or (a==n and masu[-2:]==[0,1]) \
    or (1<=a<n+1 and masu[a-2:a+1]==[0,1,0])\
    or (1<=a<n+1 and masu[a-2:a+1]==[1,0,1]) :
        ans += 1
    elif (a==1 and masu[0:2]==[0,0]) \
    or (a==n and masu[-2:]==[0,0]) \
    or (1<=a<n+1 and masu[a-2:a+1]==[0,0,0])\
    or (1<=a<n+1 and masu[a-2:a+1]==[1,1,1]) :
        ans -= 1
    print(ans)    


