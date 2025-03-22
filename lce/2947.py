# 입력
# 첫째 줄에 조각에 쓰여 있는 수가 순서대로 주어진다. 
# 숫자는 1보다 크거나 같고, 5보다 작거나 같으며, 중복되지 않는다. 처음 순서는 1, 2, 3, 4, 5가 아니다.

# 출력
# 두 조각의 순서가 바뀔때 마다 조각의 순서를 출력한다.
array = list(map(int, input().split()))

while array != [1, 2, 3, 4, 5]:
    for i in range(4): # 0 ~ 3
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
            print(' '.join(map(str, array)))
    