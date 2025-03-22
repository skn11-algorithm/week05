import sys

n = int(sys.stdin.readline().strip())
a = list(map(int,sys.stdin.readline().split()))


a_sort = sorted(list(set(a))) # 중복제거 및, 정렬

dic = {} #딕셔너리에 저장
for i in range(len(a_sort)): # 중복 제거 리스트 만큼 반복 
    dic[a_sort[i]] = i 

for i in a:
    print(dic[i],end=' ')