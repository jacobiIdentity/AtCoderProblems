#!/usr/bin/env python3
n = int(input())
aij = [input() for _ in range(n)]
ans = 0
for i in range(n) :
    ver, hor = '', ''
    for j in range(n) :
        hor += aij[i][j]
        ver += aij[j][i]
    ans = max(ans, int(hor), int(ver))
for i in range(n) :
    for j in range(n) :
        u,d,l,r,lu,ld,ru,rd = '','','','','','','',''
        for k in range(n) :
            l  += aij[i%n][(j-k)%n]
            r  += aij[i%n][(j+k)%n]
            u  += aij[(i-k)%n][j%n]
            d  += aij[(i+k)%n][j%n]
            lu += aij[(i+k)%n][(j-k)%n]
            ld += aij[(i+k)%n][(j+k)%n]
            ru += aij[(i-k)%n][(j-k)%n]
            rd += aij[(i-k)%n][(j+k)%n]
        ans = max(ans,int(l),int(r),int(u),int(d),int(lu), int(ld), int(ru), int(rd))
print(ans)
