#!/usr/bin/env python3
n,a,b = map(int,input().split())
p,q,r,s = map(int,input().split())
ans = [['.']*(s-r+1) for _ in range(q-p+1)]
# print(ans)
for i in range(q-p+1) :
    for j in range(s-r+1) :
        l1 = max(1-a,1-b)
        r1 = min(n-a,n-b)
        l2 = max(1-a,b-n)
        r2 = min(n-a,b-1)
        # print(i,j,a+l1,i+p,a+r1,b+l1,j+q,b+r1,j+q-(i+p),b-a)
        # print(i,j,a+l2,i+p,a+r2,b-r2,j+q,b-l2,j+q+(i+p),b+a) 
        if (a+l1<=i+p<=a+r1 and b+l1<=j+r<=b+r1 and j+r-(i+p)==b-a)  \
            or (a+l2<=i+p<=a+r2 and b-r2<=j+r<=b-l2 and j+r+(i+p)==b+a)  :
            ans[i][j] = '#'
# print(ans)
for i in range(q-p+1) :
    print(''.join(ans[i]))