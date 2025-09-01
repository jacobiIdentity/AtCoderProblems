#!/usr/bin/env python3
s_x,s_y = map(int,input().split())
t_x,t_y = map(int,input().split())
if s_x > t_x :
    s_x,s_y,t_x,t_y = t_x,t_y,s_x,s_y
if s_y > t_y :
    t_y = 2*s_y-t_y
if (s_x + s_y)%2 == 1 :
    s_x -= 1
if (t_x + t_y)%2 == 1 :
    t_x -= 1
n_x,n_y = s_x,s_y
ans = 0
while not(n_x == t_x and n_y == t_y) :
    stp_x = 0
    if n_x == t_x :
        ans += abs(t_y-n_y)
        n_y = t_y
        # print('if n_x == t_x :', n_x, n_y, ans)
    elif n_y == t_y :
        ans += abs(t_x-n_x)//2
        if (n_x+n_y)%2==1 and (t_x+t_y)%2==0 :
            ans += 1
        n_x = t_x
        # print('elif n_y == t_y :', n_x, n_y, ans)
    elif abs(t_x - n_x) >= abs(t_y - n_y) :
        ans += abs(t_y - n_y)
        n_x += abs(t_y-n_y)
        n_y = t_y
        # print('elif abs(t_x - n_x) >= abs(t_y - n_y) :', n_x, n_y, ans)
    else :
        ans += abs(t_x - n_x)
        n_y += abs(t_x-n_x)
        n_x = t_x
        # print("else", n_x, n_y, ans)
print(ans)