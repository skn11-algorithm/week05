'''
입력 : 다섯개의 수 
출력 : 정렬 과정과 정렬결과 

* 아이디어
앞에서부터 비교하면서 정렬하므로 버블 정렬 알고리즘을 사용한다


'''
array = list(map(int, input().split()))



for i in range(len(array) - 1):  # 전체 반복 (정렬 단계)
    for j in range(len(array) - 1 - i): 
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            print(*array) # 리스트 언패킹 


