#!/usr/bin/env python3
r_t,c_t,r_a,c_a = map(int,input().split())
d = {'U':(-1, 0),'D':(1, 0),'L':(0, -1),'R':(0, 1)}
n,m,l = map(int,input().split())
s_a_m = []
for _ in range(m):
    s, a = input().split()
    s_a_m.append((s, int(a)))
t_b_l = []
for _ in range(l):
    t, b = input().split()
    t_b_l.append((t, int(b)))

t_cnt,a_cnt = 0,0
zan_t,zan_a = s_a_m[0][1],t_b_l[0][1]
dir_t,dir_a = d[s_a_m[0][0]],d[t_b_l[0][0]]
r_t_now, c_t_now, r_a_now, c_a_now = r_t, c_t, r_a, c_a 
ans = 0
while t_cnt < m and a_cnt < l:
    k = min(zan_t, zan_a) 
    diff_r_now,diff_c_now = r_a_now - r_t_now,c_a_now - c_t_now
    diff_dir_r,diff_dir_c = dir_a[0] - dir_t[0],dir_a[1] - dir_t[1]

    if diff_dir_r == 0 and diff_dir_c == 0:
        if diff_r_now == 0 and diff_c_now == 0:
            ans += k
    elif diff_dir_r == 0:
        if diff_r_now == 0 and (-diff_c_now) % diff_dir_c == 0:
            if 1<= (-diff_c_now) // diff_dir_c <= k :
                ans += 1
    elif diff_dir_c == 0:
        if diff_c_now == 0 and (-diff_r_now) % diff_dir_r == 0:
            if 1<= (-diff_r_now) // diff_dir_r <= k :
                ans += 1
    elif (-diff_r_now) % diff_dir_r == 0 and (-diff_c_now) % diff_dir_c == 0:
            if (-diff_r_now) // diff_dir_r == (-diff_c_now) // diff_dir_c  and 1<=(-diff_c_now) // diff_dir_c<=k:
                ans += 1

    r_t_now += dir_t[0] * k
    c_t_now += dir_t[1] * k
    r_a_now += dir_a[0] * k
    c_a_now += dir_a[1] * k

    zan_t -= k
    zan_a -= k
    if zan_t == 0:
        t_cnt += 1
        if t_cnt < m:
            dir_t = d[s_a_m[t_cnt][0]]
            zan_t = s_a_m[t_cnt][1]
    if zan_a == 0:
        a_cnt += 1
        if a_cnt < l:
            dir_a = d[t_b_l[a_cnt][0]]
            zan_a = t_b_l[a_cnt][1]

print(ans)

