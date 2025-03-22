# 문자열에서 숫자의 합
def get_digit_sum(s):
    total = 0
    for char in s:
        if char.isdigit():
            total += int(char)
    return total

# 정렬 기준 함수
def sort_key(s):
    length = len(s)               
    digit_sum = get_digit_sum(s) # 위에서 정의한거
    return (length, digit_sum, s) 

n = int(input())
serials = []

for _ in range(n):
    serial = input().strip()
    serials.append(serial)

# 정렬하기
serials.sort(key=sort_key)


for s in serials:
    print(s)
