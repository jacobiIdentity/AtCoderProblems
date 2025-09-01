#!/usr/bin/env python3
n = int(input())
s = input()
ans = []
i = 0
while i < n :
    posI = s.find('/*',i)
    if posI == -1 :
        for j in range(i,n) :
            ans.append(s[j])
        break
    for j in range(i,posI) :
        ans.append(s[j])
    posJ = s.find('*/',posI+2)
    if posJ == -1 :
        for j in range(posI,n) :
            ans.append(s[j])
        break
    i = posJ+2

# while i < n :
#     if i == n-1 :
#         ans.append(s[i])
#         break
#     if s[i]=='/' and s[i+1]=='*' :
#         j = i+2
#         tmp = ['/','*']
#         while j< n :
#             if j == n-1 :
#                 tmp.append(s[j])
#                 break
#             if s[j]=='*' and s[j+1]=='/' :
#                 tmp = []
#                 i = j+1
#                 break
#             tmp.append(s[j])
#             j += 1
#         ans += tmp
#         if j == n-1 :
#             i = j
#     else :
#         ans.append(s[i])
#     i += 1
print(''.join(ans))