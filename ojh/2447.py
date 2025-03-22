N=int(input())
star_arr=[[' ']*N for _ in range(N)]

def star(x,y,N):
    if N==1:
        star_arr[x][y]='*'
        return
    
    next_N=N//3
    for i in range(3):
        for j in range(3):
            if i==1 and j==1:
                continue
            star(x+i*(next_N),y+j*(next_N),next_N)

star(0,0,N)           
for stars in star_arr:
    print(''.join(stars))


# 재귀 설계
# 1. 기저 조건 : N == 1 일때 별 하나 채우기
# 2. 재귀 분할 : 9등분하고, 중앙 부분은 비워 두고, 나머지 8개 구역에서 재귀 호출을 반복한다.
# [x][y]          [x][y+N//3]          [x][y+2*(N//3)]
# [x+N//3][y]     [x+N//3][y+N//3]     [x+N//3][y+2*(N//3)]
# [x+2*(N//3)][y] [x+2*(N//3)][y+N//3] [x+2*(N//3)][y+2*(N//3)]

# 3. 중앙 비우는 방법 : x+N//3 ~ x+2*(N//3) , y+N//3 ~ y+2*(N//3) 비우기

