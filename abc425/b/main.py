#!/usr/bin/env python3
import itertools
n = int(input())
a_n = list(map(int,input().split()))
isNo = True
for perm in itertools.permutations(range(1,n+1)) :
    p_n = list(perm)
    isOK = True
    for i in range(n) :
        if a_n[i] != -1 and p_n[i] != a_n[i] :
            isOK = False
            break
    if isOK :
        print('Yes')
        print(*p_n)
        exit()
print("No")

