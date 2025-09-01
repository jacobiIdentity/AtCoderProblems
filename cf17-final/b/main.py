#!/usr/bin/env python3
s = input()
cnts = [s.count('a'),s.count('b'),s.count('c')]
cnts.sort()
print('YNEOS'[(max(cnts)-min(cnts)>1)::2])