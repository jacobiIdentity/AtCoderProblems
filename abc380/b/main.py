#!/usr/bin/env python3
s = input()
s_n = s.split('|')
# print(s_n)
ans = [len(s_n[i]) for i in range(len(s_n))]
print(*ans[1:len(s_n)-1])
