#!/usr/bin/env python3
n,w = map(int,input().split())
cheeze = [tuple(map(int,input().split())) for _ in range(n) ]
cheeze.sort(key=lambda x:-x[0])
ans,now = 0,0
for i in range(n) :
    if now + cheeze[i][1] <= w :
        ans += cheeze[i][0]*cheeze[i][1]
        now += cheeze[i][1]
    else :
        ans += cheeze[i][0]*max(w-now,0)
        now = w
    
    if now >= w :
        break
print(ans)
