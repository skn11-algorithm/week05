import sys

N=int(sys.stdin.readline())
# 장대 start mid end
# n-1개의 원판을 start에서 mid로 옮김
# 가장 큰 원판을 end로 옮김
# n-1 개의 원판을 mid에서 end로 옮김
count=0

def hanoi(n, start, end, mid):
    global count
    count+=1
    if n==1:
        print(start, end)
        return
    hanoi(n-1,start,mid,end)
    print(start, end)
    hanoi(n-1,mid,end,start)

print(2**N-1)
if N<=20:
    hanoi(N,1,3,2)
