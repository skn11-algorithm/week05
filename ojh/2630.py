import sys
input=sys.stdin.readline

def check(x,y,N):
    # 현재 영역의 첫 번째 칸의 색상을 기준으로 설정
    color=paper[x][y]
    # 해당 영역의 모든 칸을 검사
    for i in range(x,x+N):
        for j in range(y,y+N):
            if paper[i][j]!=color:
                # 색상이 다르면 4개의 부분으로 나누어 재귀 호출
                check(x,y,N//2) # 좌상단
                check(x,y+N//2,N//2) # 우상단
                check(x+N//2,y,N//2) # 좌하단
                check(x+N//2,y+N//2,N//2) # 우하단
                return  # 재귀 호출 후 종료. 색깔 같은것만 저장해야 해서
    if color==0:
        result.append(0)
    else:
        result.append(1)

N=int(input())
paper=[]  # 색종이 정보를 저장할 리스트
result=[]  # 색종이 개수를 저장할 리스트

for _ in range(N):
    paper.append(list(map(int,input().rstrip().split())))

check(0,0,N)
print(result.count(0))
print(result.count(1))