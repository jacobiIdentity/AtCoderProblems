#!/usr/bin/env python3
s = input()
if s[0]=='1' :
    print('No')
    exit()
cols = [int(s[6]),int(s[3]),int(s[1])|int(s[7]),int(s[0])|int(s[4]),int(s[2])|int(s[8]),int(s[5]),int(s[9])]
# print(cols)
isNo = True
for i in range(len(cols)) :
    if cols[i] == 0 :
        continue
    for j in range(i+2,len(cols)) :
        if cols[j]==0 :
            continue
        for k in range(i+1,j) :
            if cols[k]==0 :
                isNo = False
print('YNeos'[isNo::2])
