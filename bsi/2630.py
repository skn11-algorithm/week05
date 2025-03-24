# # 입력받기
# n = int(input())
# lst = []
# for i in range(n): 
#     row= list(map(int, input().split()))
#     lst.append(row)

# # 분할정복 알고리즘은 복잡한 문제를 더 작은 하위 문제로 나누고, 각 하위 문제를 재귀적으로 해결한 후, 그 결과를 결합하여 원래 문제의 해를 얻는 방식입니다. 이 접근법은 컴퓨터 과학에서 효율적인 알고리즘을 설계하는 데 널리 사용됩니다.
# # 분할정복 알고리즘의 주요 단계
# # 분할 (Divide): 원래 문제를 더 작은 하위 문제로 나눕니다. 이 하위 문제들은 원래 문제와 같은 유형이어야 합니다.
# def split_lst(lst):
#     for i in len(lst):
#         for j in len(i):
#             if lst[i][j] != set(lst):       # lst안의 행렬이 다른 값들을 가지고 있다면
#                 k1, k2, k3, k4 = lst[:, i//2][:, j//2], lst[i//2, :][:, j//2], lst[:, i//2][j//2, :], lst[i//2, :][j//2, :]
#             else:
#                 lst = lst
#     return split_lst(k1), split_lst(k2), split_lst(k3), split_lst(k4)
        
# # 정복 (Conquer): 각 하위 문제를 재귀적으로 해결합니다. 하위 문제가 충분히 작아질 경우 직접 해결합니다.
# # 결합 (Combine): 하위 문제의 해를 결합하여 원래 문제의 해를 얻습니다.


def div(y, x, n): 
    color = paper[y][x] # 색종이의 색
    for i in range(y, y+n): # y 분할 
        for j in range(x, x+n): # x 분할
            if color != paper[i][j]: # 찾는 과정에서 색이 달라지면
                m = n//2
                div(y, x, m) # 색종이 분할 (2사분면)
                div(y, x + m, m) # 색종이 분할 (1사분면)
                div(y + m, x, m) # 색종이 분할 (3사분면)
                div(y + m, x + m, m) # 색종이 분할(4사분면)
                return
    if color == 0: # 흰색이면
        result[0] += 1 #자르기
    else : # 파란색이면
        result[1] += 1 # 갯수세기
        
import sys
N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 색종이
result = [0,0] # 자른 색종이 / 파란색 색종이
div(0,0,N)
print(result[0],'\n',result[1],sep='')
# 출처: https://edder773.tistory.com/116 [개발하는 차리의 학습 일기:티스토리]