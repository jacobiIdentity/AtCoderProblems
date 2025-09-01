#!/usr/bin/env python3
def calc(x) :
    if x < 10 :
        return 0
    ret = 0
    head = int(str(x)[0])
    length = len(str(x))
    for i in range(1,10) :
        for j in range(2,length) :
            ret += pow(i,j-1)
    for j in range(1,head) :
        ret += pow(j,length-1)
    for j in range(1,length) :
        if int(str(x)[j]) >= head :
            ret += pow(head,length-j)
            break
        else :
            ret += int(str(x)[j])* pow(head,length-1-j)
    isSnake  = True
    for j in str(x)[1:] :
        if  int(j) >= head :
            isSnake = False
    if isSnake :
        ret += 1
    return ret
l,r = map(int,input().split())
# print(calc(l-1))
# print(calc(r))
print(calc(r)-calc(l-1))
# f = open('myfile.txt', 'w')
# f.write('i'+chr(9)+'calc\n')
# for i in range(10,2000) :
    # f.write(str(i)+chr(9)+str(calc(i))+'\n')
    # print(i,calc(i))
# f.close()