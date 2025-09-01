n = int(input())
print(n*2)
ans = []
n *= 2
while n>0 :
    if n>7 :
        ans.append(8)
        n -= 8
    elif len(ans) :
        ans[-1] += 10*n
        break
    else :
        ans.append(n)
        break
print(''.join([str(i//2) for i in reversed(ans)]))