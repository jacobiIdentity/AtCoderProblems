#!/usr/bin/env python3
n = int(input())
s_ij = [input() for _ in range(n)]
t_ij = [input() for _ in range(n)]
s_hf,s_hl,s_wf,s_wl = n-1,0,n-1,0
t_hf,t_hl,t_wf,t_wl = n-1,0,n-1,0
for i in range(n) :
    for j in range(n) :
        if s_ij[i][j] == '#' :
            s_hf = min(s_hf,i)
            s_wf = min(s_wf,j)
            s_hl = max(s_hl,i)
            s_wl = max(s_wl,j)
        if t_ij[i][j] == '#' :
            t_hf = min(t_hf,i)
            t_wf = min(t_wf,j)
            t_hl = max(t_hl,i)
            t_wl = max(t_wl,j)
# print(s_hf,s_hl,s_wf,s_wl)
# print(t_hf,t_hl,t_wf,t_wl)
s_ajdust1 = [list(s_ij[i][s_wf:s_wl+1]) for i in range(s_hf,s_hl+1)]
t_ajdust1 = [list(t_ij[i][t_wf:t_wl+1]) for i in range(t_hf,t_hl+1)]
s_ajdust2 = [list(reversed((s_ij[i][s_wf:s_wl+1]))) for i in reversed(range(s_hf,s_hl+1))]
t_ajdust2 = [list(reversed((t_ij[i][t_wf:t_wl+1]))) for i in reversed(range(t_hf,t_hl+1))]
s_ajdust3 = [[s_ij[j][i] for j in range(s_hf,s_hl+1)] for i in reversed(range(s_wf,s_wl+1))]
t_ajdust3 = [[t_ij[j][i] for j in range(t_hf,t_hl+1)] for i in reversed(range(t_wf,t_wl+1))]
s_ajdust4 = [[s_ij[j][i] for j in reversed(range(s_hf,s_hl+1))] for i in range(s_wf,s_wl+1)]
t_ajdust4 = [[t_ij[j][i] for j in reversed(range(t_hf,t_hl+1))] for i in range(t_wf,t_wl+1)]
# print(s_ajdust1)
# print(s_ajdust2)
# print(s_ajdust3)
# print(s_ajdust4)
# print(t_ajdust1)
# print(t_ajdust2)
# print(t_ajdust3)
# print(t_ajdust4)
s_candidates = [s_ajdust1,s_ajdust2,s_ajdust3,s_ajdust4]
t_candidates = [t_ajdust1,t_ajdust2,t_ajdust3,t_ajdust4]
for s_c in s_candidates :
    for t_c in t_candidates :
        if s_c == t_c :
            print('Yes')
            # print(s_c)
            # print(t_c)
            exit()
print('No')
# print(s_ajdust1)
# print(s_ajdust2)
# print(s_ajdust3)
# print(s_ajdust4)