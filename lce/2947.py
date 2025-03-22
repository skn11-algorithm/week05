array = list(map(int, input().split()))


while array != [1, 2, 3, 4, 5]:
    for i in range(4): # 0 ~ 3
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
            print(' '.join(map(str, array)))
    