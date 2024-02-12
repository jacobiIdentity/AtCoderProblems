#!/usr/bin/env python3
ha, wa = map(int, input().split())
a_h = [input() for _ in range(ha)]
hb, wb = map(int, input().split())
b_h = [input() for _ in range(hb)]
hx, wx = map(int, input().split())
x_h = [input() for _ in range(hx)]
fha, lha, fwa, lwa = -1, -1, -1, -1
fhb, lhb, fwb, lwb = -1, -1, -1, -1
fhx, lhx, fwx, lwx = -1, -1, -1, -1
dA = set()
dB = set()
dX = set()
for i in range(ha) :
    for j in range(wa) :
        if a_h[i][j] == '#' :
            fha = i if fha == -1 else fha
            fwa = j if fwa == -1 else fwa
            lha = max(lha, i)
            lwa = max(lwa, j)
for i in range(hb) :
    for j in range(wb) :
        if b_h[i][j] == '#' :
            fhb = i if fhb == -1 else fhb
            fwb = j if fwb == -1 else fwb
            lhb = max(lhb, i)
            lwb = max(lwb, j)
for i in range(hx) :
    for j in range(wx) :
        if x_h[i][j] == '#' :
            fhx = i if fhx == -1 else fhx
            fwx = j if fwx == -1 else fwx
            lhx = max(lhx, i)
            lwx = max(lwx, j)
newA = [a_h[i][fwa:lwa+1] for i in range(fha, lha+1)]
newB = [b_h[i][fwb:lwb+1] for i in range(fhb, lhb+1)]
newX = [x_h[i][fwx:lwx+1] for i in range(fhx, lhx+1)]
print(newA, sep="\n")
print(newB, sep="\n")
print(newX, sep="\n")