#!/usr/bin/env python3
n = int(input())
ac, wa, tle,re = 0,0,0,0
for _ in range(n) :
    s = input()
    if s == 'AC' :
        ac += 1
    elif s == 'WA' :
        wa += 1
    elif s == 'TLE' :
        tle += 1
    else :
        re += 1
print('AC x {}'.format(ac))
print('WA x {}'.format(wa))
print('TLE x {}'.format(tle))
print('RE x {}'.format(re))