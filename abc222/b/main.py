#!/usr/bin/env python3
n,p = map(int,input().split())
print(len(list(filter(lambda x:x<p,[p+1]+list(map(int,input().split()))))))
