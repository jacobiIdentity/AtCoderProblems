#!/usr/bin/env python3
n, x = map(int, input().split())
a_n = set(list(map(int, input().split())))
flg = False
for a in a_n :
    if a - x in a_n or a + x in a_n :
        flg = True
print('Yes' if flg else 'No')