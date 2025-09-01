#!/usr/bin/env python3
n,x = map(int,input().split())
l_n = [0]+list(map(int,input().split()))
# print(l_n)
# O(n)解法
# i = 1
# while i<n+1 :
#     l_n[i] += l_n[i-1]
#     if l_n[i]>x:
#         break
#     i+=1
# print(i)
# O(log(n))解法 と言いつつ、↑ O(n)だから意味ない
ok,ng=0,n+1
while ng-ok>1 :
    mid = (ok+ng)//2
    if l_n[mid] <= x :
        ok = mid
    else :
        ng = mid
    # print(ok,ng)
print(ok+1)