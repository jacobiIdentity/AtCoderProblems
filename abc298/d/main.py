import math
q = int(input())
a = '1'
top = a[0]
for _ in range(q) :
    query = input()
    if query[0] == '1' :
        a = a + query[2]
    elif query[0] == '2' :
        a = a.replace(top, '', 1)
        top = a[0]
    else :
        print(int(a)%998244353)
