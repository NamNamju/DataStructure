class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None
        self.height = 0  # 높이 정보도 유지함에 유의!!

    def __str__(self):
        return str(self.key)


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def preorder(self, v):
        if v != None:
            print(v.key, end=' ')
            self.preorder(v.left)
            self.preorder(v.right)

    def inorder(self, v):
        if v != None:
            self.inorder(v.left)
            print(v.key, end=' ')
            self.inorder(v.right)

    def postorder(self, v):
        if v != None:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key, end=' ')

    def find_loc(self, key):  # if key is in T, return its Node
        # if not in T, return the parent node under where it is inserted
        if self.size == 0: return None
        p = None  # p = parent node of v
        v = self.root
        while v:  # while v != None
            if v.key == key:
                return v
            else:
                if v.key < key:
                    p = v
                    v = v.right
                else:
                    p = v
                    v = v.left
        return p

    def search(self, key):
        p = self.find_loc(key)
        if p and p.key == key:
            return p
        else:
            return None

    def insert(self, key):
        v = Node(key)
        if self.size == 0:
            self.root = v
            self.size += 1
        else:
            p = self.find_loc(key)
            if p and p.key != key:  # p is parent of v
                if p.key < key:
                    p.right = v
                else:
                    p.left = v
                v.parent = p
                self.size += 1
        self.height(v)
        return v

    # 노드들의 height 정보 update 필요

    def deleteByMerging(self, x) :
        # assume that x is not None
        if x == None:
            return None
        a, b, pt = x.left, x.right, x.parent

        if a == None:
            c = b
        else:  # a != None
            c = m = a
            # find the largest leaf m in the subtree of a
            while m.right:
              m = m.right
            m.right = b
            if b: b.parent = m


        if self.root == x:  # c becomes a new root
            if c: c.parent = None
            self.root = c
        else:  # c becomes a child of pt of x
            if pt.left == x:
                pt.left = c
            else:
                pt.right = c
            if c: c.parent = pt
        self.size -= 1

    # 노드들의 height 정보 update 필요

    def deleteByCopying(self, x):
        if x == None:
            return None
        a, b, pt = x.left, x.right, x.parent

        if self.root == x:
            if a != None:
                y = a
                while y.right:
                    y = y.right
                x.key = y.key
                if y.left != None:
                    y.left.parent = y.parent
                    if y.parent.right == y:
                        y.parent.right = y.left
                    else:
                        y.parent.left = y.left
                else:
                    if y.parent.right == y:
                        y.parent.right = None
                    else:
                        y.parent.left = None

            elif a == None and b != None:
                b.parent == None
                self.root = b
            else:
                self.root = None
        else:
            if a != None:
                y = a
                while y.right:
                    y = y.right
                x.key = y.key
                if y.left != None:
                    y.left.parent = y.parent
                    if y.parent.right == y:
                        y.parent.right = y.left
                    else:
                        y.parent.left = y.left
                else:
                    if y.parent.right == y:
                        y.parent.right = None
                    else:
                        y.parent.left = None


            elif a == None and b != None:
                y = b
                while y.left:
                    y = y.left
                x.key = y.key
                if y.right != None:
                    t = y.right
                    t.parent = x
                    x.right = t
                else:
                    if y.parent.right == y:
                        y.parent.right = None
                    else:
                        y.parent.left = None
            else:
                if pt.left == x:
                    pt.left = None
                else:
                    pt.right = None
        self.size -= 1

    # 노드들의 height 정보 update 필요

    def height(self, x):  # 노드 x의 height 값을 리턴
        if x == None:
            return -1
        else:
            left_h = self.height(x.left)
            right_h = self.height(x.right)
            return 1 + max(left_h,right_h)

    def succ(self, x):  # key값의 오름차순 순서에서 x.key 값의 다음 노드(successor) 리턴
        if x != None:
            if x == self.root and x.right == None:
                return None
            else:
                a = self.root
                if a.right != None:
                    while a.right != None:
                        a = a.right
                if x == a:
                    return None
                else:
                    if x.right != None:
                        x = x.right
                        while x.left != None:
                            x = x.left
                    else:
                        while x != x.parent.left:
                            x = x.parent
                        x = x.parent
        else :
            return None
        return x
        '''
        if x!= None:
            if x == self.root:
                if x.right != None:
                    return x.right
                else:
                    return None
            else:
                if x.right != None:
                    return x.right
                elif x.parent.left != None and x.parent.left == x:
                    return x.parent
                else:
                    return None
        else:
            return None

    # x의 successor가 없다면 (즉, x.key가 최대값이면) None 리턴
    '''

    def pred(self, x):  # key값의 오름차순 순서에서 x.key 값의 이전 노드(predecssor) 리턴
        if x != None:
            if x == self.root and x.left == None:
                return None
            else:
                a = self.root
                if a.left != None:
                    while a.left != None:
                        a = a.left
                if x == a:
                    return None
                else:
                    if x.left != None:
                        x = x.left
                        while x.right != None:
                            x = x.right
                    else:
                        while x != x.parent.right:
                            x = x.parent
                        x = x.parent
        else:
            return None
        return x
        '''
        if x != None:
            if x == self.root:
                if x.left != None:
                    return x.left
                else:
                    return None
            else:
                if x.left != None:
                    return x.left
                elif x.parent.right != None and x.parent.right == x:
                    return x.parent
                else:
                    return None
        else:
            return None
'''

    # x의 predecessor가 없다면 (즉, x.key가 최소값이면) None 리턴


    def rotateLeft(self, x):  # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
        z = x.right  # assume that z != None
        if z == None: return  # if x == None: nothing changed
        b = z.left  # b == None 인 경우도 가능
        z.parent = x.parent
        if x.parent:
            if x.parent.left == x:
                x.parent.left = z
            else:
                x.parent.right = z
        if z: z.left = x
        x.parent = z
        x.right = b
        if b: b.parent = x
        # z == self.root라면 x가 새로운 루트가 되어야 함!
        if x == self.root and x != None:
            self.root = z

    def rotateRight(self, z):  # rotateLeft도 유사하게 정의
        x = z.left  # assume that z != None
        if x == None: return  # if x == None: nothing changed
        b = x.right  # b == None 인 경우도 가능
        x.parent = z.parent
        if z.parent:
            if z.parent.left == z:
                z.parent.left = x
            else:
                z.parent.right = x
        if x: x.right = z
        z.parent = x
        z.left = b
        if b: b.parent = z
        # z == self.root라면 x가 새로운 루트가 되어야 함!
        if z == self.root and z != None:
            self.root = x
    # [주의] height가 있다면 x와 z의 height 값을 수정하는 코드 추가 필요


T = BST()
while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'deleteC':
        v = T.search(int(cmd[1]))
        T.deleteByCopying(v)
        print("- {0} is deleted by copying".format(int(cmd[1])))
    elif cmd[0] == 'deleteM':
        v = T.search(int(cmd[1]))
        T.deleteByMerging(v)
        print("- {0} is deleted by merging".format(int(cmd[1])))
    elif cmd[0] == 'search':
        v = T.search(int(cmd[1]))
        if v == None:
            print("* {0} is not found!".format(cmd[1]))
        else:
            print("* {0} is found!".format(cmd[1]))
    elif cmd[0] == 'height':
        h = T.height(T.search(int(cmd[1])))
        if h == -1:
            print("= {0} is not found!".format(cmd[1]))
        else:
            print("= {0} has height of {1}".format(cmd[1], h))
    elif cmd[0] == 'succ':
        v = T.succ(T.search(int(cmd[1])))
        if v == None:
            print("> {0} is not found or has no successor".format(cmd[1]))
        else:
            print("> {0}'s successor is {1}".format(cmd[1], v.key))
    elif cmd[0] == 'pred':
        v = T.pred(T.search(int(cmd[1])))
        if v == None:
            print("< {0} is not found or has no predecssor".format(cmd[1]))
        else:
            print("< {0}'s predecssor is {1}".format(cmd[1], v.key))
    elif cmd[0] == 'Rleft':
        v = T.search(int(cmd[1]))
        if v == None:
            print("@ {0} is not found!".format(cmd[1]))
        else:
            T.rotateLeft(v)
            print("@ Rotated left at node {0}".format(cmd[1]))
    elif cmd[0] == 'Rright':
        v = T.search(int(cmd[1]))
        if v == None:
            print("@ {0} is not found!".format(cmd[1]))
        else:
            T.rotateRight(v)
            print("@ Rotated right at node {0}".format(cmd[1]))
    elif cmd[0] == 'preorder':
        T.preorder(T.root)
        print()
    elif cmd[0] == 'postorder':
        T.postorder(T.root)
        print()
    elif cmd[0] == 'inorder':
        T.inorder(T.root)
        print()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")
