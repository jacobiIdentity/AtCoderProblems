#!/usr/bin/env python3
n, p, q = map(int, input().split())
print(min([p]+list(map(lambda x:x+q, map(int, input().split())))))
