#스택

import sys

input = sys.stdin.readline

i = int(input())
a=[]
for _ in range(i):
    sen=input().split()
    if (sen[0] == 'push'):
        a.append(sen[1])
    elif(sen[0] == 'pop'):
        if not a:
            print(-1)
        else:
            print(a.pop())
    elif (sen[0] == 'size'):
        print(len(a))
    elif (sen[0] == 'empty'):
        if not a:
            print(1)
        else:
            print(0)
    elif (sen[0] == 'top'):
        if not a:
            print(-1)
        else:
            print(a[len(a)-1])




