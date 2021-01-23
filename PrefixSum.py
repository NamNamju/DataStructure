import time, random

def prefixSum1(X, n):
	# code for prefixSum1
	for i in range(n):
		S[i] = 0
		for j in range(i+1):
			S[i] += X[j]
	
def prefixSum2(X, n):
	# code for prefixSum2
	S[0] = X[0]
	for i in range(n):
		S[i] = S[i-1] + X[i]
	
random.seed()		# random 함수 초기화
# n 입력받음
# 리스트 X를 randint를 호출하여 n개의 랜덤한 숫자로 채움
# prefixSum1 호출
# prefixSum2 호출
# 두 함수의 수행시간 출력

n = input()
n = int(n)
X=[random.randint(-999,999) for r in range(n)]

S = [0 for i in range(n)]
before1 = time.clock()
prefixSum1(X, n)
after1 = time.clock()

S = [0 for i in range(n)]
before2 = time.clock()
prefixSum2(X, n)
after2 = time.clock()

print(after1-before1, after2-before2)

