from collections import defaultdict
import sys
s = input()
n = int(input())
if int(s.replace('?', '0'),base=2) > n :
    print(-1)
    exit()
sList = ['0']*(max(0,len(format(n,'b'))-len(s)))+list(s)
for i in range(len(sList)) :
    if sList[i] != '?' :
        continue
    tmp = int(''.join(sList[:i])+'1'+s[i+1:].replace('?','0'),base=2)
    if tmp > n :
        sList[i]= '0'
    else :
        sList[i]= '1'
print(int(''.join(sList),base=2))
