n = int(input())
s = input()
t, a = 0, 0
half = n//2 + n%2
for i in range(n) :
    if s[i] == 'T' :
        t += 1
    else :
        a += 1
    if a >= half or t >= half:
        break
print('T' if t >= half else 'A')