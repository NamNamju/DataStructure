class Node:

    def __init__(self, key=None):
        self.key = key
        self.prev = self
        self.next = self

    def __str__(self):
        return str(self.key)


class DoublyLinkedList:

    def __init__(self):
        self.head = Node()
        self.size = 0


    def __len__(self):
        return self.size


    def __iter__(self):
        v = self.head
        while v != None:
            yield v
            v = v.next


    def __str__(self):
        return " -> ".join(str(v) for v in self)


    def splice(self, a, b, x): #가장 중요한 함수. a-b구간을 잘라서 x-xn 사이에 집어넣는다.
        if a == None or b == None or x == None:
            return

        ap = a.prev
        bn = b.next

        # cut
        ap.next = bn
        bn.prev = ap

        # insert
        xn = x.next
        xn.prev = b
        b.next = xn
        a.prev = x
        x.next = a


    def moveBefore(self, a, x): # node a를 node x 앞으로 이동
        self.splice(a, a, x.prev)


    def insertBefore(self, x, key):# node x 앞에 key인 새 node를 삽입
        self.moveBefore(Node(key), x)
        self.size += 1


    def pushBack(self, key):  # data가 key인 새 node를 생성해 마지막에 node를 삽입함. 즉, self.head 앞에 삽입함.
        self.insertBefore(self.head, key)


    def deleteNode(self, x): # Node 삭제 함수
        t = self.search(x) # search를 통해 x 값을 갖는 Node를 찾는다.
        if  t== None or t == self.head:
            return # 바로 종료
        k = self.head.next # k에 front_node 저장
        while (k != self.head): # 한 바퀴를 돌 때까지
            if k.key == t.key:
                break
            k = k.next
        k.prev.next, k.next.prev = k.next, k.prev # Node끼리 이어주기
        del k
        self.size -= 1

    def search(self, k): # 탐색 함수
        if self.size == 0:
            return None
        else:
            x = self.head.next # front_node 저장
            while (x != self.head): # 한 바퀴 돌 때까지
                if x.key == k:
                    break
                x = x.next
            if x.key == k:
                return x
            else:
                return None


def josephus(n, k):
    # DoublyLinkedList 클래스 인스탠스 L을 선언
    L = DoublyLinkedList()

    # 1번부터 n번까지의 key 값을 갖는 노드를 pushBack 함수를 써서 L에 삽입
    for i in range(1, n+1):
        L.pushBack(i)

    # k개의 링크를 따라간 노드를 remove하는 과정을 한 노드만 남을때까지 반복.
    # 주의: k개의 링크를 따라갈때 dummy노드도 방문될수 있다는 점

    temp = L.head.next # key가 어디서부터 시작하면 되는지 저장한다.
    key = L.head.next # n번째인 key값을 저장하고 삭제한다.

    while (L.size != 1):
        t = temp # 시작점
        count = k # n번 while문을 돌기 위해 count로 센다.

        while (count != 0):
            key = t
            t = t.next # 옆 node로 이동
            if key == L.head: # head_node는 None이므로 삭제할 수 없다.
                continue
            count -= 1
        temp = key.next # key는 삭제 될 예정이므로 시작점은 key의 다음 node이다.
#        print(key.key)
        L.deleteNode(key.key)



    # 남아 있는 노드의 key를 리턴
    return L.head.next.key


# n과 k를 입력
n, k = map(int, input('').split())
# n과 k에 대해서 Josephus함수 호출에서 리턴값을 출력
print(josephus(n, k))