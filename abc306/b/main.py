#!/usr/bin/env python3
a_n = list(map(int, input().split()))
ans = 0
b = 1
for aa in a_n :
    ans += aa*b
    b *= 2
print(ans)