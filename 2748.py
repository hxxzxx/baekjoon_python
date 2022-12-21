#import sys

#input = sys.stdin.readline

n=int(input())

def fibo(n):
    val=[0,1]
    for i in range(2,n+1):
        val.append(val[i-1]+val[i-2])
    return val[n]

print(fibo(n))