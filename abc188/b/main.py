#!/usr/bin/env python3
n = int(input())
a_n =list( map(int,input().split()))
b_n =list( map(int,input().split()))
print('YNeos'[sum(map(lambda x:x[0]*x[1],zip(a_n,b_n)))!=0::2])