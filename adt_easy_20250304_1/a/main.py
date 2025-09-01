#!/usr/bin/env python3
abc = list(map(int,input().split()))
abc2 = sorted(abc)
print('YNeos'[not(abc[1]==abc2[1])::2])