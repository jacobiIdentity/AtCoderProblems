#!/usr/bin/env python3
n = int(input())
a_n= list(map(int,input().split()))
print(sum([0]+list(filter(lambda x:x>0,[a_n[i+1]-a_n[i] for i in range(n-1)]))),-sum([0]+list(filter(lambda x:x<0,[a_n[i+1]-a_n[i] for i in range(n-1)]))))