#!/usr/bin/env python3
s = input()
t = input()
len1s = {'AB','BC', 'CD', 'DE', 'EA',\
         'BA','CB', 'DC', 'ED', 'AE'}
print('Yes' if ((s in len1s) and (t in len1s)) or ((s not in len1s) and (t not in len1s)) else 'No')