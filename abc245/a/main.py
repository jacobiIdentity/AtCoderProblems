#!/usr/bin/env python3
a,b,c,d = map(int,input().split())
print('Takahashi' if a<c or (a==c and b<=d) else 'Aoki')