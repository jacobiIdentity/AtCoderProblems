#!/usr/bin/env python3
n, m = map(int, input().split())
a_b = []
s = input()
t = input()
diff = (ord(t[0]) - ord(s[0]))%26
isYes = True
for i in range(len(s)) :
    if diff != (ord(t[i]) - ord(s[i]))%26 :
        isYes = False
print("Yes" if isYes else "No")