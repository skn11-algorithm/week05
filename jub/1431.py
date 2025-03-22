# 리스트 정렬해야됨으로 sort 함수 사용


n = int(input())
s = [] #시리얼 번호 저장할 빈 리스트
d = dict() # 시리얼 번호 숫자합을 저장할 빈 딕셔너리

for i in range (n): #n 만큼 반복하는 루프
    a = input() # 시리얼 번호 입력
    temp = 0
    s.append(a) # 시리얼 번호 저장

    for c in a: #a 각 문자에 대해 루프 
        if c in '123456789': #숫자가 있으면 
            temp += int(c) # 해당 숫자를 더함 
    d[a] = temp #숫자합을 딕셔너리에 저장 

# data 리스트 정렬, 길이, 숫자합, 사전 순
# lambda 익명 함수 생성 
s.sort(key = lambda x : (len(x),d[x],x))

for i in s: # s 리스트 각 항목 반복 
    print(i) #출력
  
  
  
  
  
  
