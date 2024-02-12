n = int(input())
s = input()
ans = -1
tmp = 0
for i in range(n) :
    if s[i] == 'o' :
        tmp += 1
    if s[i] == '-' :
        ans = max(tmp, ans)
        tmp = 0
if s[n-1] == 'o' and n-1-tmp >= 0 and s[n-1-tmp] == '-' :
    ans = max(ans, tmp)
if ans == 0 :
    ans = -1
print(ans)