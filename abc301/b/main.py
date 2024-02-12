n = int(input())
a_n = list(map(int, input().split()))
ans = []
now = 0
while now < n-1 :
    if abs(a_n[now] - a_n[now+1]) == 1 :
        ans.append(a_n[now])
    elif a_n[now] < a_n[now+1]:
        for i in range(a_n[now],a_n[now+1]) :
            ans.append(i)            
    else :
        for i in range(a_n[now],a_n[now+1], -1) :
            ans.append(i)            
    now += 1
ans.append(a_n[now])
print(*ans)