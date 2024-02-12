#!/usr/bin/env python3
n = int(input())
a_n = [-1]+list(map(int, input().split()))
p_n = [-1]*2+list(map(int, input().split()))
cnt = 0
fst = a_n[1]
while cnt < 100 :
    for i in range(2,n+1) :
        a_n[p_n[i]] = a_n[p_n[i]]+ a_n[i]
    # print(a_n[1:])
    cnt += 1
if fst == a_n[1] :
    print(a_n[1] if a_n[1] == 0 else ('+' if a_n[1]> 0 else '-'))
elif fst > a_n[1] :
    print('-')
else :
    print('+')