def stick(one,three,n):
    if n == 1:
        print(one,three)
        return

    stick(one, 6-one-three, n-1) #1단계 (1->2)
    print(one, three) #2단계 (마지막원반 1->3)
    stick(6-one-three, three, n-1) #3단계 (2->3)

#메인
n = int(input())
print(2**n-1)
if n <= 20:
    stick(1,3,n)
    