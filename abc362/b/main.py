#!/usr/bin/env python3
xa,ya = map(int,input().split())
xb,yb = map(int,input().split())
xc,yc = map(int,input().split())
ab2 = (xa-xb)**2 + (ya-yb)**2
bc2 = (xb-xc)**2 + (yb-yc)**2
ca2 = (xc-xa)**2 + (yc-ya)**2
print('Yes' if (ab2+bc2-ca2==0)or (bc2+ca2-ab2==0)or (ca2+ab2-bc2==0) else 'No')

