'''
입력 : 정사각형 종이의 한 변의 길이 N
출력 : 잘린 흰색 색종이(0) 개수 / 파란색 색종이(1) 개수

아이디어
- 문제는 대표적인 분할정복의 예시(머지소트)
- 가로세로를 n/2만큼 나눴을 때 같은 수로 채워져있을 때까지 n/2를 반복 (재귀함수)
'''

import sys
n = int(sys.stdin.readline())

# 리스트 함축을 통한 사각형 배열 만들기 
square = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
white = 0
blue = 0

def divide(x, y, n):
    global white, blue
    color = square[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color!= square[i][j]:
                divide(x, y, n//2)
                divide(x, y + n//2, n//2)
                divide(x + n//2, y, n//2)
                divide(x + n//2, y + n//2, n//2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1

divide(0, 0, n)
print(white)
print(blue)