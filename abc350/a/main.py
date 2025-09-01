#!/usr/bin/env python3
# n = int(input()[3:])
# print('Yes' if n <= 349 and n != 316 else 'No')

s = input()
pastABCs = ['ABC'+ '%03d'%(i) for i in range(1,350)]
pastABCs.remove('ABC316')
print('Yes' if s in pastABCs else 'No')