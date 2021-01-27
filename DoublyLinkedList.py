# 1. class Node 선언 부분
class Node:
    def __init__(self, key=None):
        self.key = key
        self.prev = self
        self.next = self


    def __str__(self):
        return str(self.key)

# 2. class DoublyLinkedList 선언부분
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

    def splice(self, a, b, x):
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

    def moveAfter(self, a, x):  # node a를 node x 뒤로 이동
        self.splice(a, a, x)

    def moveBefore(self, a, x):
        self.splice(a, a, x.prev)

    #

    def insertAfter(self, x, key):  # node x 뒤에 key인 새 node를 삽입
        self.moveAfter(Node(key), x)
        self.size += 1

    def insertBefore(self, x, key):
        self.moveBefore(Node(key), x)
        self.size += 1

    def pushFront(self, key):  # data가 key인 새 node를 생성해 head(dummy node) 다음 삽입, 즉 front head가 된다.
        self.insertAfter(self.head, key)

    def pushBack(self, key):  # head 이전에 삽입
        self.insertBefore(self.head, key)

    #

    def deleteNode(self, x):
        if x == None or x == self.head:
            return
        k = self.head.next
        while (k != self.head) :
            if k.key == x.key:
                break
            k = k.next
        k.prev.next, k.next.prev = k.next, k.prev
        del k
        self.size -= 1

    def popFront(self):
        if self.head.next == self.head:
            return None
        key = self.head.next
        self.deleteNode(key)
        self.size -= 1
        return key.key

    def popBack(self):
        if self.head.next == self.head:
            return None
        key = self.head.prev
        self.deleteNode(key)
        self.size -= 1
        return key.key

    #
    def search(self, k):
        if self.size == 0:
            return None
        else:
            x = self.head.next
            while (x != self.head) :
                if x.key == k:
                    break
                x = x.next
            if x.key == k :
                return x
            else:
                return None

    def first(self):
        if self.size == 0:
            return None
        else:
            return self.head.next.key

    def last(self):
        if self.size == 0:
            return None
        else:
            return self.head.prev.key

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
    #

    def printList(self):  # 변경없이 사용할 것!
        v = self.head
        count = 0
        while (v):
            if count == 0 and v.key == None:
                print("h ->", end=" ")
            elif count > 0 and v.key == None:
                print("h")
                break
            else:
                print(v.key, "->", end=" ")
            v = v.next
            count += 1


L = DoublyLinkedList()
while True:
    cmd = input().split()
    if cmd[0] == 'pushF':
        L.pushFront(int(cmd[1]))
        print("+ {0} is pushed at Front".format(cmd[1]))
    elif cmd[0] == 'pushB':
        L.pushBack(int(cmd[1]))
        print("+ {0} is pushed at Back".format(cmd[1]))
    elif cmd[0] == 'popF':
        key = L.popFront()
        if key == None:
            print("* list is empty")
        else:
            print("- {0} is popped from Front".format(key))
    elif cmd[0] == 'popB':
        key = L.popBack()
        if key == None:
            print("* list is empty")
        else:
            print("- {0} is popped from Back".format(key))
    elif cmd[0] == 'search':
        v = L.search(int(cmd[1]))
        if v == None:
            print("* {0} is not found!".format(cmd[1]))
        else:
            print(" * {0} is found!".format(cmd[1]))
    elif cmd[0] == 'insertA':
        # inserta key_x key : key의 새 노드를 key_x를 갖는 노드 뒤에 삽입
        x = L.search(int(cmd[1]))
        if x == None:
            print("* target node of key {0} doesn't exit".format(cmd[1]))
        else:
            L.insertAfter(x, int(cmd[2]))
            print("+ {0} is inserted After {1}".format(cmd[2], cmd[1]))
    elif cmd[0] == 'insertB':
        # inserta key_x key : key의 새 노드를 key_x를 갖는 노드 앞에 삽입
        x = L.search(int(cmd[1]))
        if x == None:
            print("* target node of key {0} doesn't exit".format(cmd[1]))
        else:
            L.insertBefore(x, int(cmd[2]))
            print("+ {0} is inserted Before {1}".format(cmd[2], cmd[1]))
    elif cmd[0] == 'delete':
        x = L.search(int(cmd[1]))
        if x == None:
            print("- {0} is not found, so nothing happens".format(cmd[1]))
        else:
            L.deleteNode(x)
            print("- {0} is deleted".format(cmd[1]))
    elif cmd[0] == "first":
        print("* {0} is the value at the front".format(L.first()))
    elif cmd[0] == "last":
        print("* {0} is the value at the back".format(L.last()))
    elif cmd[0] == 'print':
        L.printList()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")
