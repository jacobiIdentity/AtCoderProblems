#!/usr/bin/env python3
n,m,k = map(int,input().split())
isNo = True
# ↓が O(n)解法
if (m%2==0 or n%2==0) and m*n==2*k :
    isNo = False
for i in range(n+1) :
    if 2*i-n!=0 and (m*n-2*k)%(2*i-n)==0 and \
        ((m*n-2*k)//(2*i-n)+m)%2==0 and 0<= ((m*n-2*k)//(2*i-n)+m)//2 <= m :
        isNo = False
        break

# ↓が O(m*n)解法
# bs = {0}
# for i in range(n+1) :
#     for j in range(m+1) :
#         bs.add(i*m+j*n-2*i*j)
#         if i*m+j*n-2*i*j == k :
#             isNo = False
#             break
#     if not(isNo) :
#         break
print('YNeos'[isNo::2])