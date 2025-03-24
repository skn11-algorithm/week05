# 색종이 만들기

# 문제
# 정사각형은 하얀색 혹은 파란색으로 칠해져 있음
# 절반씩 잘라가며 색종이를 나눔

# input: 종이의 한 변의 길이 N \n 색종이의 가로줄이 차례로 (흰색은 0, 파란색은 1)
# output: 잘라진 하얀색 색종이의 개수 출력, 파란색 색종이의 개수 출력

# 문제 풀이
# 1. 종이 자르기: if line[i][j] != line[i][j+1], n/2
# 2. 종이 자르면 4개가 무조건 나오니까 재귀함수로 각 종이들의 좌표를 넣기
# 3. 재귀 함수 빠져 나와서 1이면 파랑+1, 0이면 흰색+1

# 시간 복잡도: O(n^2)

import sys

input = sys.stdin.readline

def divide_and_conquer(x, y, n):
    global white, blue
    color = paper[x][y]
    
    for xi in range(x, x+n):
        for yi in range(y, y+n):
            if color != paper[xi][yi]:
                divide_and_conquer(x, y, n//2)
                divide_and_conquer(x+n//2, y, n//2)
                divide_and_conquer(x, y+n//2, n//2)
                divide_and_conquer(x+n//2, y+n//2, n//2)
                return 
    
    if color == 0:
        white += 1
    else:
        blue += 1
        
if __name__ == '__main__':
    n = int(input())
    paper = [list(map(int, input().split())) for _ in range(n)]
    white, blue = 0,0   
     
    divide_and_conquer(0,0,n)

    print(white, blue, sep='\n')        