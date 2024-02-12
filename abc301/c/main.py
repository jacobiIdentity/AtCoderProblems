from collections import defaultdict
import sys
s = input()
t = input()
s_d = defaultdict(int)
t_d = defaultdict(int)
for i in range(len(s)) :
    s_d[s[i]] += 1
    t_d[t[i]] += 1
sCnt, tCnt = s_d['@'], t_d['@']
for i in range(26) :
    tmp = chr(ord('a')+i)
    if tmp in ['a','t','c','o','d','e','r'] :
        if s_d[tmp] < t_d[tmp] :
            s_d['@'] -= (t_d[tmp] -s_d[tmp])
        elif s_d[tmp] > t_d[tmp] :
            t_d['@'] -= (s_d[tmp] - t_d[tmp])
        if s_d['@'] < 0 or t_d['@'] < 0 :
            print('No')
            exit()
    elif s_d[tmp] != t_d[tmp] :
        print('No')
        exit()
print('Yes' if s_d['@'] == t_d['@'] else 'No')
            

    