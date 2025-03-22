# import sys
# input = sys.stdin.readline

# n = int(input())
# # lst = []
# llst = []
# lst = list(map(int, input().split()))

# for i in lst:
#     count = 0
#     lllst = lst
#     lllst = list(set(lllst))
#     for j in range(len(lllst)):
#         if i > lllst[j]:
#             count += 1
#     llst.append(count)

# print(*llst)

# 딥시크로 시간 줄이기
import sys
import bisect

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

# 중복 제거 후 정렬
sorted_unique = sorted(set(lst))
# 각 원소에 대해 이진 탐색으로 개수 계산
result = [bisect.bisect_left(sorted_unique, x) for x in lst]

print(*result)
# 변경 사항 설명:

# bisect 모듈을 사용하여 정렬된 리스트에서 효율적으로 원소의 위치를 찾습니다.
# 중복 제거 및 정렬을 한 번만 수행하여 불필요한 반복 작업을 제거했습니다.
# 리스트 컴프리헨션을 사용하여 간결하고 빠르게 결과를 생성합니다.
# 이 방법은 기존의 O(n²) 알고리즘을 O(n log n)으로 개선하여 큰 입력 크기에서도 빠르게 실행됩니다.