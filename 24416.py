import sys

input = sys.stdin.readline

n = int(input())


def fib(n):
    if (n == 1 or n == 2):
        return (1)
    else:
        return (fib(n-1)+fib(n-2))

def fibo(n):
    val=[0,1]
    cnt = 0
    for i in range(2,n+1):
        cnt += 1
        val.append(val[i-1]+val[i-2])
    return (val)



print(fib(n),fibo(n))
