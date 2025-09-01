#!/usr/bin/env python3

s = input()
# s = list(input())
# s.reverse()
tgt = 'AKIHABARA'
i,j = 0,0
aPos = [0,4,6,8]
isNo = True
for i in range(1<<4) :
    tmp = list(tgt)
    for j in range(4) :
        if i&(1<<j) :
            tmp[aPos[j]] = ''
    # print(s, ''.join(tmp))
    if ''.join(tmp) == s :
        isNo = False
print('YNEOS'[isNo::2])

# tmp = ''
# while s :
#     v = s.pop()
#     if i == len(tgt) :
#         print('No')
#         exit()
#     elif v==tgt[i] :
#         tmp += v
#         i += 1
#         continue
#     elif tgt[i] == 'A' :
#         tmp += 'A'
#         s.append(v)
#         i += 1
#         continue
#     else :
#         print('NO')
#         exit()
# print('YNEOS'[(tgt!=tmp and tgt!=tmp+'A')::2])
# if len(s) > len(tgt) :
#     print('NO')
#     exit()
# while i<len(s)+1 and i+j<len(tgt) :
#     if i<len(s) and s[i]==tgt[i+j] :
#         tmp += s[i]
#         i += 1
#     elif tgt[i+j]=='A' :
#         tmp += 'A'
#         j += 1
#     else :
#         print('NO')
#         exit()
# # print(tmp)
# print('YNEOS'[not(tgt==tmp and i>=len(s)-1)::2])
