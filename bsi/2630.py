n = int(input())
lst = []
for i in range(n): 
    row= list(map(int, input().split()))
    lst.append(row)

print(lst)