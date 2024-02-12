n = int(input())
l, r = 1, n
while r - l != 1 :
    m = (l+r)//2
    print('? '+str(m))
    if input()  == '0' :
        l = m
    else :
        r = m
print('! '  + str(l))