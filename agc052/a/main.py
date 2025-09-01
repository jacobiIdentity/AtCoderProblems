#!/usr/bin/env python3
t = int(input())
for _ in range(t) :
    n = int(input())
    s1 = input()
    s2 = input()
    s3 = input()
    s1 += s1
    s2 += s2
    s3 += s3
    pos1,pos2,pos3 = -1,-1,-1
    ans = ''
    for i in range(2*n+1):
        if  max(s1.find('0',pos1+1),s2.find('0',pos2+1),s3.find('0',pos3+1)) <= max(s1.find('1',pos1+1),s2.find('1',pos2+1),s3.find('1',pos3+1)) :
            ans += '0'
            pos1,pos2,pos3 = s1.find('0',pos1+1),s2.find('0',pos2+1),s3.find('0',pos3+1)
        else :
            ans += '1'
            pos1,pos2,pos3 = s1.find('1',pos1+1),s2.find('1',pos2+1),s3.find('1',pos3+1)
    print(ans)