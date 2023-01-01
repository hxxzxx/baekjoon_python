#주사위 세개

a,b,c=map(int, input().split())

def cal(a,b,c):
    if (a == b and a == c) :
        reward=10000+a*1000
    elif (a == b or a == c):
        reward=1000+a*100
    elif (b == c):
        reward=1000+b*100
    else:
        if (a > b ):
            if (a > c):
                max = a
            else:
                max = c
        elif ( a < b):
            if (b > c):
                max =b
            else:
                max = c
        reward = max *100
    return(reward)

print(cal(a,b,c))
