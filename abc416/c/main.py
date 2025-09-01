#!/usr/bin/env python3
n,k,x = map(int,input().split())
s_n = [input() for _ in range(n)]
ans = []
for i in range(n**k) :
    f = []
    # fPos = [0]*k
    j = i
    while j >0 or len(f)<k :
        if j == 0 :
            f.append(s_n[0])
            continue
        f.append(s_n[j%n])
        j //= n
    # print(f)
    ans.append(''.join(f))
print(sorted(ans)[x-1])