import sys
nums=list(map(int,sys.stdin.readline().rstrip().split()))

for i in range(5):
    for j in range(4):
        if nums[j]>nums[j+1]:
            temp=nums[j]
            nums[j]=nums[j+1]
            nums[j+1]=temp
            print(*nums)