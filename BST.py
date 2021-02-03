# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None

    def __str__(self):
        return str(self.key)


class Tree:
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
        return v

    def deleteByMerging(self, x) :
        # assume that x is not None
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
    def deleteByCopying(self,x):
        a, b, pt = x.left, x.right, x.parent

        if self.root == x:
            if a != None:
                y = a
                while y.right:
                    y = y.right
                x.key = y.key
                if y.left != None:
                    y.left.parent = y.parent
                    y.parent.right = y.left
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
                    y.parent.right = y.left
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


T = Tree()

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
        if v == None: print("* {0} is not found!".format(cmd[1]))
        else: print(" * {0} is found!".format(cmd[1]))
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