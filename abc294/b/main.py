#!/usr/bin/env python3
h, w = map(int, input().split())
a_ij =  [list(map(int, input().split())) for _ in range(h)]
for i in range(h) :
    ans = ''
    for j in range(w) :
        ans += '.' if a_ij[i][j] == 0 else chr(a_ij[i][j]-1+ord('A'))
    print(ans)

