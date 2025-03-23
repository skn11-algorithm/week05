'''
# 좌표 압축 

아이디어-> 값 하나를 모두와 비교하며 len값 뽑아야하므로
1. 중복값을 없앤다음에 리스트로 재변환
2. 반복문을 통해 요소를 순회하면서 작은값(좌표) 찾기 

입력 : 입력개수 / 입력값

출력 : 자신보다 작은 수의 개수, len값 
'''
n = int(input().strip())
y_array = list(map(int, input().strip().split()))

del_duplicate = set(y_array) # 같은 값은 같은 좌표를 가지므로 중복 없애주고
new_array = list(del_duplicate) # 없앤 중복을 다시 리스트로 바꿔줌
new_array.sort() # 새로운 배열을 차례대로 sort 

dic = {} # 딕셔너리로 인덱스와 값을 정렬시켜준다

for i in range(len(new_array)): 
  dic[new_array[i]] = i # 배열의 0번째는 0, 1번째는 자기가 1, 2번째는 2 

for i in y_array:
  print(dic[i], end=' ')