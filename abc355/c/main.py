#!/usr/bin/env python3
n,t = map(int,input().split())
a_n = list(map(int,input().split()))
cols = [0]*n
rows = [0]*n
diags = [0]*2
diag0 = [n*(i-1)+i for i in range(1,n+1)] 
diag1 = [n*(n-i)+i for i in range(1,n+1)] 
for i in range(t) :
    cols[(a_n[i]-1)//n] += 1
    rows[a_n[i]%n] += 1
    if a_n[i] in diag0 :
        diags[0] += 1
    if a_n[i] in diag1 :
        diags[1] += 1
    if cols[(a_n[i]-1)//n] == n or rows[a_n[i]%n] == n or diags[0] == n or diags[1] == n :
        print(i+1)
        exit()
    # print(cols)
    # print(rows)
    # print(diags)
print(-1)
