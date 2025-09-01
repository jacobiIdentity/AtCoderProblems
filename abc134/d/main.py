#!/usr/bin/env python3
n = int(input())
a_n  = list(map(int,input().split()))
ans = []
for i in reversed(range(n)) :
    if a_n[i] :
        ans.append(i+1)
        j = 1
        while j*j <= (i+1) :
            if (i+1)%j == 0 :
                a_n[j-1] = 1-a_n[j-1]
                if j != (i+1)//j :
                    a_n[(i+1)//j-1] = 1-a_n[(i+1)//j-1]
            j+=1
print(len(ans))
if len(ans)>0 :
    print(*sorted(ans))
