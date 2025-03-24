'''
피보나치 수 출력
'''

n= int(input())
    
def pivo(n):
	if n <= 1:
		return n
	else:
		return pivo(n-1) + pivo(n-2)
	
print(pivo(n))