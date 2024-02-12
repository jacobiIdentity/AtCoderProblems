#!/usr/bin/env python3
a_ij = [input().split() for _ in range(9)]
digits = set(['1','2','3','4','5','6','7','8','9'])
for k in range(9) :
    if {a_ij[k][j] for j in range(9)} != digits :
        print('No')
        # print(k)
        # print({a_ij[k][j] for j in range(9)} != digits)
        # print({a_ij[k][j] for j in range(9)} )
        # print(digits)
        exit()
    if {a_ij[i][k] for i in range(9)} != digits :
        print('No')
        # print(k)
        # print({a_ij[i][k] for i in range(9)} != digits)
        # print({a_ij[i][k] for i in range(9)} )
        # print(digits)
        exit()
for a in range(3) :
    for b in range(3) :
        if {a_ij[(a-1)*3+c][(b-1)*3+d] for c in range(3) for d in range(3)} != digits :
            print('No')
            exit()
print('Yes')
    
