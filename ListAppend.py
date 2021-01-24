def append(value): # value를 매개변수로 갖는 append 함수를 작성한다.
    global capacity, n, count, A, B
    # 함수 안에서 global로 전역변수를 선언하여 함수 밖에서도 사용할 수 있도록 한다.

    if n == capacity: # ‘만약 n과 capacity가 같다면’ 이라는 조건으로 if문을 작성한다.
        capacity = capacity * 2 # capacity에 capacity의 두배 만큼의 용량을 할당해준다.
        #용량(capacity)만큼 n이 다 차있기 때문에 더 큰 용량을 할당받아야 한다.
        B = [None]*capacity # capacity 크기의 B라는 새로운 리스트를 만든다.
        for i in range(n): # n 범위의 for문을 작성한다.
            B[i] = A[i] # A 리스트 안의 값들을 B 리스트로 옮긴다.
            count += 1 # A 리스트 안의 값들을 B 리스트로 옮기는 동안에 발생하는 이사비용을 계산한다. (1씩 추가해준다.)
        del A # A 리스트를 지운다.
        A = B # B 리스트의 이름을 A로 바꾼다.
    A[n] = value # A[n]에 value 값을 집어넣는다.
    n = n + 1 # n에 값이 하나 더 들어갔기 때문에 n+1로 값이 증가한다.
    count += 5 # 이사 비용 이외에 5번의 기본 연산이 필요하다고 가정하고 count를 5 추가해준다.

# append 함수 종료

count = 0  
capacity = 1
n = 0
N = int(input("Number of append operations = ")) # append 연산을 수행할 N 값을 입력한다.
A = [None] # 리스트 사이즈가 1인 A 리스트를 만든다.
B = [] # 비어 있는 B 리스트를 만든다.
for i in range(N): # N 범위의 for문을 작성한다.
    append(i) # 함수를 호출하고 인자로 i를 전달한다.
print(N, "append operations need", count, "basic operations in total, so average cost per append is", count/N)