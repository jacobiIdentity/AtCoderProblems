#!/usr/bin/env python3
s_ = list(input())
t = list(input())
candidates = []
# print(len(s_))
# print(len(t))
ans = []
for i in range(len(s_)-len(t)+1) :
    isCandidate = True
    s = s_[:i]
    for j in range(len(t)) :
        if s_[i+j]!=t[j] and s_[i+j] != '?' :
            # print(i,j,s_[i+j],t[j])
            isCandidate = False
            break
        else :
            s.append(t[j])
    if isCandidate :
        s += s_[i+len(t):]
        ans.append("".join(s).replace('?','a'))
if len(ans) == 0 :
    print('UNRESTORABLE')
    exit()
ans.sort()
print(ans[0])

# for i in range(len(s_)-len(t)+1) :
#     isCandidate = True
#     for j in range(len(t)) :
#         if s_[i+j]!=t[j] and s_[i+j] != '?' :
#             # print(i,j,s_[i+j],t[j])
#             isCandidate = False
#             break
#     if isCandidate :
#         candidates.append(i)
# ans = []
# for i in candidates :
#     s = [ss for ss in s_]
#     for j in range(len(t)) :
#         s[i+j] = t[j]
#     ans.append(''.join(s).replace('?','a'))
# if len(ans) == 0 :
#     print('UNRESTORABLE')
#     exit()
# ans.sort()
# print(ans[0])
# print(ans)