import sys
input=sys.stdin.readline
n=int(input())
nums=list(map(int,input().rstrip().split()))
result={num:i for i,num in enumerate(sorted(set(nums)))}
print(' '.join(map(str,[result[num] for num in nums])))
