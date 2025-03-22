# n = int(input())
# lst = []
# for _ in range(n):
#     lst.append(input())

# # 길이순으로 나열
# lst.sort(key = len)

# # 숫자 순
# def keep_numbers(s):
#     return ''.join([char for char in s if char.isdigit()])

# lst_key = []
# for i in lst:
#     sum = 0
#     l = keep_numbers(i)
#     for j in l:
#         if j == []:
#             sum = i
#         else:
#             sum += int(j)
#     lst_key.append(sum)

# # 숫자의 합 키로 주기, 순서대로 나열
# dict_lst = dict(sorted(zip(lst_key, lst)))

# print(dict_lst)     # {0: 'ABCD', 6: 'Z321', 10: 'A910'}

# https://hongcoding.tistory.com/61
n = int(input())

def sum_num(inputs):
    result = 0
    for i in inputs:
        if i.isdigit():
            result+=int(i)
    return result

arr = []
for i in range(n):
    a = input()
    arr.append(a)

arr.sort(key = lambda x:(len(x), sum_num(x), x))
for i in arr:
    print(i)



# n = int(input())

# arr = []
# for i in range(n):
#     a = input()
#     arr.append(a)


# for i in range(n-1):
#     for j in range(i+1, n):
#         # 짧은 것이 먼저
#         if len(arr[i]) > len(arr[j]):
#             arr[i], arr[j] = arr[j], arr[i]

#         elif len(arr[i]) == len(arr[j]):
#             suma=0
#             sumb=0
#             for x,y in zip(arr[i],arr[j]):
#                 if x.isdigit():
#                     suma+=int(x)
#                 if y.isdigit():
#                     sumb+=int(y)
#             if suma > sumb:
#                 arr[i],arr[j] = arr[j], arr[i]

#             elif suma == sumb:
#                 for x,y in zip(arr[i], arr[j]):
#                     if x > y:
#                         arr[i],arr[j] = arr[j], arr[i]
#                         break
#                     elif x < y:
#                         break


# for i in arr:
#     print(i)