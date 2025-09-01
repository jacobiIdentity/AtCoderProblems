#!/usr/bin/env python3
a,b = map(int,input().split())
print(-1 if len({a,b}) == 1 else list({1,2,3}-{a,b}).pop())