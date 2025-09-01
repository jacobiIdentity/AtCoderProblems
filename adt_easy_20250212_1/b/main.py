#!/usr/bin/env python3
print(input().replace('0','x').replace('1','0').replace('x','1'))
# print(''.join([ str(int(ss)^1) for ss in list(input())]))
# print(''.join(['1' if ss=='0' else '0' for ss in list(input())]))