#!/usr/bin/env python3
repunits = []
tmp = 1
for _ in range(12) :
    repunits.append(tmp)
    tmp = tmp*10 + 1
trios = set()
for r1 in repunits :
    for r2 in repunits :
        for r3 in repunits :
            trios.add(r1+r2+r3)
print(sorted(list(trios))[int(input())-1])
