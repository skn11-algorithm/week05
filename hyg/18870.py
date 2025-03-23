# 좌표 압축
# input: N(좌표 개수) \n 좌표들
# output: 입력받은 좌표를 압축한 결과

# 문제
# 수직선 위에 n개의 좌표
# 좌표 압축: xi'의 개수 ==  xi>xj를 만족하는 서로 다른 xj의 개수
# xi에 좌표 압축을 적용해 xi'로 만들어 출력하자

# 각 좌표를 크기 순으로 순서를 매긴 다음 출력하기
# 겹치는 원소 없도록
# 빨리 찾아야 하니까 dict 사용

import sys

input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

s = set(l)
result = list(s)
result.sort()

d = {}
for i in range(len(result)):
    d[result[i]] = i

for i in l:
    print(d[i], end=' ')