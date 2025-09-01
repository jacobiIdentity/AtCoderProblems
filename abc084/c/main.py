#!/usr/bin/env python3
n = int(input())
c_s_f = [list(map(int,input().split())) for _ in range(n-1)]
ans = [0]
for i in reversed(range(n-1)) :
    tmp = 0
    for j in range(i,n-1) :
        c,s,f = c_s_f[j][0],c_s_f[j][1],c_s_f[j][2]
        tmp = ((max(tmp,s)+f-1)//f)*f +c
    ans.append(tmp)
ans.reverse()
print(*ans,sep="\n")