n = int(input())
nums = list(map(int, input().split()))

sorted_unique = sorted(set(nums))

rank = {num: idx for idx, num in enumerate(sorted_unique)}

print(' '.join(str(rank[num]) for num in nums))
