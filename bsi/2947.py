lst = list(map(int, input().split()))

for i in range(1, len(lst)):
    for j in range(0, len(lst) - i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
            print(*lst)
