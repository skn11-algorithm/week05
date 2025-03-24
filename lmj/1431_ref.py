'''
# 시리얼 번호

# 입력 : 기타개수 / 시리얼 번호 
# 출력 : sort된 시리얼 번호 

# 아이디어
# 시리얼 번호는 알파벳 대문자와 숫자로 구성되어 있다
# 1. 길이가 짧은 것 먼저
# 2. 길이가 같다면 숫자합 작은것이 먼저
# 3. 숫자 < 알파벳

# 몰랐던 개념 
숫자구분 => isdigit !!!

'''

n = int(input()) 
arr = []

for i in range(n):  
    serial = input() 
    if len(serial) <= 50:  
        arr.append(serial)  

def num_sum(string): # 문자열의 합 
    result = 0
    for i in string:
        if i.isdigit():  
            result += int(i) 
    return result

arr.sort(key=lambda x: (len(x), num_sum(x), x))  # 길이, 숫자 합, 알파벳 순으로 정렬


for serial in arr:
    print(serial)