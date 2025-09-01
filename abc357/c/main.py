#!/usr/bin/env python3
def base_n(num_10,n):
    str_n = ['0']*6
    for i in reversed(range(6)) :
        str_n[i] = str(num_10%3)
        # print(i,num_10)
        num_10 //= n
    return ''.join(str_n)
n = int(input())
for i in range(3**n) :
    i_3 = base_n(i, 3)
    ans = ''
    for j in range(3**n) :
        j_3 = base_n(j, 3) 
        isWhite = False
        for k in range(6) :
            if i_3[k] == j_3[k] and i_3[k]=='1' :
                isWhite = True
        ans += '.' if isWhite else '#'
    print(ans)

