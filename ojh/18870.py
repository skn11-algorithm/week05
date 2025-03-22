import sys
input=sys.stdin.readline
n=int(input())
nums=list(map(int,input().rstrip().split()))

# 중복 처리 # 10 9 10 9
index_map={}
for i,num in enumerate(sorted(set(nums))): # 중복 없애고 정렬 # 9 10
    index_map[num]=i # 9 : 0, 10 : 1

for i in range(n):
    nums[i]=index_map[nums[i]]
print(*nums)



