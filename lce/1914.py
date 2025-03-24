import sys
sys.setrecursionlimit(10000)

n = int(input())

print(2 ** n - 1)

if n <= 20:
    def hanoi(n, start, end):
        if n == 1:
            print(f"{start} {end}")
            return
        mid = 6 - start - end 
        hanoi(n - 1, start, mid)
        print(f"{start} {end}")
        hanoi(n - 1, mid, end)

    hanoi(n, 1, 3)
