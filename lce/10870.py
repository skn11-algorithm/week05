def fibo ():
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n+1)

n = input(int())
