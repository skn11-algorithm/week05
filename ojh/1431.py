import sys

def issum(input):
    hap=0
    for i in input:
        if i.isdigit():
            hap+=int(i)
    return hap

input=sys.stdin.readline
N=int(input().rstrip())
nums=[]
for _ in range(N):
    nums.append(input().rstrip())

# arr.sort(key=function) 정렬 기준 정의
# 길이, 숫자 합, 알파벳 순으로 정렬
nums.sort(key=lambda x:(len(x),issum(x),x))
print("\n".join(nums))