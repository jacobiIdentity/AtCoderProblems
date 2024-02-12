#!/usr/bin/env python3
a, x, m = map(int, input().split())
print(x%m if a == 1 else ((pow(a,x,(a-1)*m)-1)%((a-1)*m))//(a-1))
