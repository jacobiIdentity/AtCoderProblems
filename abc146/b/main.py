#!/usr/bin/env python3
n = int(input())
s = input()
ans = ''
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
for ss in s :
    ans +=  alphabets[(ord(ss)-ord('A')+n)%26]
print(ans)