# n = int(input())
# lst= [[[], [], []], [[], [], []], [[], [], []]]
# def stars(n):
#     if n == 3:
#         k = '*'
#         for a in range(3):
#             lst[0][a] = k
#         lst[1][0] = k 
#         lst[1][2] = k     
#         for a in range(3):
#             lst[2][a] = k
#     else:
#         k = stars(n//3)
#         for a in range(3):
#             lst[0][a] = k
#         lst[1][0] = k 
#         lst[1][2] = k     
#         for a in range(3):
#             lst[2][a] = k
# stars(n)
# print(lst)

import sys
sys.setrecursionlimit(10**6)

def append_star(LEN):
    if LEN == 1:
        return ['*']

    Stars = append_star(LEN//3) 
    L = []  
    
    for S in Stars:
        L.append(S*3)
    for S in Stars:
        L.append(S+' '*(LEN//3)+S)
    for S in Stars:
        L.append(S*3)
    return L

n = int(sys.stdin.readline().strip())
print('\n'.join(append_star(n)))
# 출처: https://cotak.tistory.com/38 [TaxFree:티스토리]