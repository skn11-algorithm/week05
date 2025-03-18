# 별찍기 10

# 문제
# 재귀적인 패턴으로 별 찍기
# 패턴은 nxn 크기의 정사각형 모양
# n이 3보다 크면, n의 패턴은 공백으로 채워진 가운데의 n/3 x n/3 정사각형을 n/3 패턴으로 둘러싼 형태

# input: n (n은 3의 거듭제곱)
# output: n번째 줄까지 별 출력하기

# 문제 풀이
# (n//3, n//3, n//3 * 2, n//3 * 2)의 좌표가 비어있어야 함 (x,y,x,y)
# 분할 정복으로 쪼개서 생각하기

def divide_and_conquer(x,y,n):
    global arr
    if n==1:
        arr[x][y] = '*'
        return
        
    divide_and_conquer(x,y,n//3)
    divide_and_conquer(x+n//3,y,n//3)
    divide_and_conquer(x+(n//3)*2,y,n//3)
    
    divide_and_conquer(x,y+n//3,n//3)
    # divide_and_conquer(x+n//3,y+n//3,n//3)
    divide_and_conquer(x+(n//3)*2,y+n//3,n//3)
    
    divide_and_conquer(x,y+(n//3)*2,n//3)
    divide_and_conquer(x+n//3,y+(n//3)*2,n//3)
    divide_and_conquer(x+(n//3)*2,y+(n//3)*2,n//3)
    

if __name__ == '__main__':
    n = int(input())
    arr=[[' ' for j in range(n)] for i in range(n)]
    divide_and_conquer(0,0,n)
    
    for a in arr:
        for ai in a:
            print(ai, end='')
        print()
    