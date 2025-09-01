#!/usr/bin/env python3
n,m = map(int,input().split())
a_b = [list(map(int,input().split())) for _ in range(m)]
a_b.sort(key=lambda x:(x[0]-x[1],x[0]))
# print(a_b)
now,i,ans = 0,0,0
while i<m :
    a,b = a_b[i][0],a_b[i][1]
    if n>=a :
        cnt = (n-a)//(a-b)+1
        # if (n-a)%(a-b) :
        #     cnt += 1
        ans += cnt
        n -= (a-b)*cnt
        # print(n,ans,a,b)
    i+=1
print(ans)
