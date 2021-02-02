class Heap:
    def __init__(self, L=[]):
        self.A = L

    def __str__(self):
        return str(self.A)

    def __len__(self):
        return len(self.A)

    def make_heap_max(self): # 최댓값
        n = len(self.A)
        for k in range(n - 1, -1, -1):  # A[n-1] → ... → A[0]
            self.heapify_max(k, n)

    def make_heap_min(self): # 최솟값
        n = len(self.A)
        for k in range(n - 1, -1, -1):  # A[n-1] → ... → A[0]
            self.heapify_min(k, n)

    def heapify_max(self, k, n): #최댓값
        # n = 힙의 전체 노드수 [heap_sort를 위해 필요함]
        # A[k]가 힙 성질을 위배한다면, 밑으로
        # 내려가면서 힙성질을 만족하는 위치를 찾는다

        while 2 * k + 1 < n:  # [❓] 조건문이 어떤 뜻인가?
            L, R = 2 * k + 1, 2 * k + 2  # [❓] L, R은 어떤 값?
            if L < n and self.A[L] > self.A[k]:
                m = L
            else:
                m = k
            if R < n and self.A[R] > self.A[m]:
                m = R  # m = A[k], A[L], A[R] 중 최댓값의 인덱스
            if m != k:  # A[k]가 최댓값이 아니라면 힙 성질 위배
                self.A[k], self.A[m] = self.A[m], self.A[k]
                k = m
            else:
                break  # 왜 break할까?

    def heapify_min(self, k, n): # 최솟값
        # n = 힙의 전체 노드수 [heap_sort를 위해 필요함]
        # A[k]가 힙 성질을 위배한다면, 밑으로
        # 내려가면서 힙성질을 만족하는 위치를 찾는다

        while 2 * k + 1 < n:  # [❓] 조건문이 어떤 뜻인가?
            L, R = 2 * k + 1, 2 * k + 2  # [❓] L, R은 어떤 값?
            if L < n and self.A[L] < self.A[k]:
                m = L
            else:
                m = k
            if R < n and self.A[R] < self.A[m]:
                m = R  # m = A[k], A[L], A[R] 중 최솟값의 인덱스
            if m != k:  # A[k]가 최솟값이 아니라면 힙 성질 위배
                self.A[k], self.A[m] = self.A[m], self.A[k]
                k = m
            else:
                break  # 왜 break할까?

    def delete_max(self): # 최대힙에서 max delete
        if len(self.A) == 0: return None
        key = self.A[0]
        self.A[0], self.A[len(self.A) - 1] = self.A[len(self.A) - 1], self.A[0]
        self.A.pop()  # 실제로 리스트에서 delete!
        self.heapify_max(0, len(self.A))  # len(self.A) = n-1
        return

    def delete_min(self): #최소힙에서 min delete
        if len(self.A) == 0: return None
        key = self.A[0]
        self.A[0], self.A[len(self.A) - 1] = self.A[len(self.A) - 1], self.A[0]
        self.A.pop()  # 실제로 리스트에서 delete!
        self.heapify_min(0, len(self.A))  # len(self.A) = n-1
        return
################################################################################################

    def heapify_max_up(self, k):  # 올라가면서 A[k]를 재배치. 최대힙
        while k > 0 and self.A[(k - 1) // 2] < self.A[k]:
            self.A[k], self.A[(k - 1) // 2] = self.A[(k - 1) // 2], self.A[k]
            k = (k - 1) // 2

    def heapify_min_up(self, k):  # 올라가면서 A[k]를 재배치. 최소힙
        while k > 0 and self.A[(k - 1) // 2] > self.A[k]:
            self.A[k], self.A[(k - 1) // 2] = self.A[(k - 1) // 2], self.A[k]
            k = (k - 1) // 2

    def insert_max(self, key): # 최대힙에 원소 삽입
        self.A.append(key)
        self.heapify_max_up(len(self.A) - 1)

    def insert_min(self, key): # 최소힙에 원소 삽입
        self.A.append(key)
        self.heapify_min_up(len(self.A) - 1)

def median_fun(S):
    maxList = []
    minList = []
    maxHeap = Heap() #최대힙
    minHeap = Heap() #최소힙
    sum = 0
    
    for i in range(len(S)):
        if len(maxHeap) == 0 and len(minHeap) == 0:
            maxList.append(S[i])
            maxHeap.__init__(maxList)
            maxHeap.make_heap_max()
        elif len(maxHeap) == 1 and len(minHeap) == 0:
            minList.append(S[i])
            minHeap.__init__(minList)
            minHeap.make_heap_min()
        else:
            if len(maxHeap) == len(minHeap) :
                maxHeap.insert_max(S[i])
            else:
                minHeap.insert_min(S[i])

        if len(minHeap) != 0 and len(maxHeap) != 0 and minHeap.A[0] < maxHeap.A[0] :
            tempA = maxHeap.A[0]
            tempB = minHeap.A[0]

            maxHeap.delete_max()
            minHeap.delete_min()

            maxHeap.insert_max(tempB)
            minHeap.insert_min(tempA)

            #maxList.remove(tempA)
            #maxList.append(tempB)

            #minList.remove(tempB)
            #minList.append(tempA)

            #maxHeap.__init__(maxList)
            #minHeap.__init__(minList)

            #maxHeap.make_heap_down()
            #minHeap.make_heap_up()

        #print("maxHeap", maxHeap, "minHeap", minHeap)
        #print(maxHeap.A[0])

        sum += maxHeap.A[0]


    return sum

S = [int(x) for x in input().split()]
print(median_fun(S))