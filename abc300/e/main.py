from collections import defaultdict
n = int(input())
d = defaultdict(int)
while True :
    if n%2 == 0 :
        n //= 2
        d[2] += 1
    elif n%3 == 0 :
        n //= 3
        d[3] += 1
    elif n%5 == 0 :
        n //= 5
        d[5] += 1
    elif n == 1 :
        break
    else :
        print(0)
        exit()
print(d)