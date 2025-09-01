#!/usr/bin/env python3
n,x = map(int,input().split())
machines = [list(map(int,input().split())) for _ in range(n)]
ans = 0
tmpCosts = 0
tmpW = float('inf')
for i in range(n) :
    if machines[i][1] < machines[i][3] :
        tmpCosts += machines[i][1]
        tmpW = min(machines[i][0],tmpW)
    elif machines[i][3] < machines[i][1] :
        tmpCosts += machines[i][3]
        tmpW = min(machines[i][2],tmpW)
    elif machines[i][0] < machines[i][2] :
        tmpCosts += machines[i][3]
        tmpW = min(machines[i][2],tmpW)
    else :
        tmpCosts += machines[i][1]
        tmpW = min(machines[i][0],tmpW)
if tmpCosts <= x :
    ans = tmpW
print(ans)

productivities = [[] for i in range(n)]
for i in range(n) :
    