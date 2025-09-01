#!/usr/bin/env python3
n,q = map(int,input().split())
x_q = list(map(int,input().split()))
box = [0]*n
ans = []
for i in range(q) :
    x = x_q[i]
    if x>=1 :
        box[x-1]+= 1
        ans.append(x)
    else :
        tmp,now = 101,-1
        for j in range(n) :
            if box[j] < tmp :
                tmp = box[j]
                now = j
        # print(tmp,now)
        box[now] += 1
        ans.append(now+1)
print(*ans)