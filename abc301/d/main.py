from collections import defaultdict
import sys
s = input()
n = int(input())
if int(s.replace('?', '0'),base=2) > n :
    print(-1)
    exit()
if int(s.replace('?', '1'),base=2) < n+1 :
    print(int(s.replace('?', '1'),base=2))
    exit()
if len(s) > len(bin(n)[2:]):
    s = s[len(s)-len(bin(n)[2:]):]
q = s.count('?')
t = s
while q > 0 :
    if int(s.replace('?', '1', 1).replace('?', '0')) < n :
        t = t.replace('?', '1', 1)
    else :
        t = t.replace('?', '0', 1)
    q = t.count('?')
print(int(t))
