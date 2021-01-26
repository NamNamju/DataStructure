class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None

    def __str__(self):
        return str(self.key)


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def printList(self):  # 변경없이 사용할 것!
        v = self.head
        while (v):
            print(v.key, "->", end=" ")
            v = v.next
        print("None")

    def pushFront(self, key):
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node
        self.size += 1


    def pushBack(self, key):
        new_node = Node(key)
        if self.size == 0:
            self.head = new_node
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = new_node
        self.size += 1


    def popFront(self):
        # head 노드의 값 리턴. empty list이면 None 리턴
        if self.size == 0:
            return None
        else:
            x = self.head
            key = x.key
            self.head = x.next
            self.size = self.size - 1
            del x
            return key


    def popBack(self):
        # tail 노드의 값 리턴. empty list이면 None 리턴
        if self.size == 0:
            return None
        else:
            prev, tail = None, self.head
            while tail.next != None:
                prev = tail
                tail = tail.next
            if prev == None:  # 리스트에 노드가 하나
                self.head = None
            else:
                prev.next = tail.next  # 즉, None
            key = tail.key
            del tail
            self.size -= 1
            return key


    def search(self, key):
        # key 값을 저장된 노드 리턴. 없으면 None 리턴
        v = self.head
        while v != None:
            if v.key == key:
                return v
            v = v.next
        return v


    def remove(self, x):
        # 노드 x를 제거한 후 True리턴. 제거 실패면 False 리턴
        # x는 key 값이 아니라 노드임에 유의!
        v = self.head
        if self.size == 0:
            return False
        else:
            if self.head == x:
                self.head = v.next
                self.size -= 1
                del v
                return True
            else:
                if x == None:
                    return False
                else:
                    prev = None
                    while v != x:
                        prev = v
                        v = v.next
                    prev.next = v.next
                    del v
                    self.size -= 1
                    return True


    def reverse(self):
      node_head = self.head
      v = None
      while (node_head != None) :
          r = node_head.next
          node_head.next = v
          v = node_head
          node_head = r
      self.head = v


    def findMax(self):
        # self가 empty이면 None, 아니면 max key 리턴
        v = self.head
        if self.size == 0:
            return None
        else:
            max_key = v.key
            while v != None:
                if max_key < v.key:
                    max_key = v.key
                v = v.next
            return max_key


    def deleteMax(self):
        # self가 empty이면 None, 아니면 max key 지운 후, max key 리턴
      if self.size == 0 :
        return None
      else:
        max_key = self.findMax()
        max_key_index = self.search(max_key)
        self.remove(max_key_index)
        return max_key

    def insert(self, k, val):
        new_node = Node(val)
        if self.size == 0:
            self.head = new_node
            self.size += 1
        elif self.size < k:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = new_node
            self.size += 1
        else:
            v = self.head
            prev = None
            count = 0
            while count != k:
                count += 1
                prev = v
                v = v.next
            if count == 0:
              new_node.next = self.head
              self.head = new_node
              self.size += 1
            else:
              prev.next = new_node
              new_node.next = v
              self.size += 1


    def size(self):
        return self.size


# 아래 코드는 수정하지 마세요!
L = SinglyLinkedList()
while True:
    cmd = input().split()
    if cmd[0] == "pushFront":
        L.pushFront(int(cmd[1]))
        print(int(cmd[1]), "is pushed at front.")
    elif cmd[0] == "pushBack":
        L.pushBack(int(cmd[1]))
        print(int(cmd[1]), "is pushed at back.")
    elif cmd[0] == "popFront":
        x = L.popFront()
        if x == None:
            print("List is empty.")
        else:
            print(x, "is popped from front.")
    elif cmd[0] == "popBack":
        x = L.popBack()
        if x == None:
            print("List is empty.")
        else:
            print(x, "is popped from back.")
    elif cmd[0] == "search":
        x = L.search(int(cmd[1]))
        if x == None:
            print(int(cmd[1]), "is not found!")
        else:
            print(int(cmd[1]), "is found!")
    elif cmd[0] == "remove":
        x = L.search(int(cmd[1]))
        if L.remove(x):
            print(x.key, "is removed.")
        else:
            print("Key is not removed for some reason.")
    elif cmd[0] == "reverse":
        L.reverse()
    elif cmd[0] == "findMax":
        m = L.findMax()
        if m == None:
            print("Empty list!")
        else:
            print("Max key is", m)
    elif cmd[0] == "deleteMax":
        m = L.deleteMax()
        if m == None:
            print("Empty list!")
        else:
            print("Max key", m, "is deleted.")
    elif cmd[0] == "insert":
        L.insert(int(cmd[1]), int(cmd[2]))
        print(cmd[2], "is inserted at", cmd[1] + "-th position.")
    elif cmd[0] == "printList":
        L.printList()
    elif cmd[0] == "size":
        print("list has", len(L), "nodes.")
    elif cmd[0] == "exit":
        print("DONE!")
        break
    else:
        print("Not allowed operation! Enter a legal one!")