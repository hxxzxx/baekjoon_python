import sys

input = sys.stdin.readline
a,b,c=map(int, input().split())

temp =max(a,b,c)
def cal(a,b,c):
    if (a == b and a == c) :
        reward=10000+a*1000
    elif (a == b or a == c):
        reward=1000+a*100
    elif (b == c):
        reward=1000+b*100
    else:
        reward =temp *100
    return(reward)

print(cal(a,b,c))
