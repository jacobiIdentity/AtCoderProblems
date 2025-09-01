#!/usr/bin/env python3
n,t,a = map(int,input().split())
print('Yes' if (n-t-a)+min(t,a)<max(t,a) else 'No')