class HashOpenAddr:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None]*self.size
        self.values = [None]*self.size
    def __str__(self):
        s = ""
        for k in self:
            if k == None:
                t = "{0:5s}|".format("")
            else:
                t = "{0:-5d}|".format(k)
            s = s + t
        return s
    def __iter__(self):
        for i in range(self.size):
            yield self.keys[i]

    def find_slot(self, key):
        i = self.hash_function(key) # key 값을 갖는 hash의 index인듯.
        start = i
        while (self.keys[i] != None) and (self.keys[i] != key) :
            i = (i + 1) % self.size
            if (i == start) :
                return None
        return i

    def set(self, key, value=None): # 삽입 연산
        i = self.find_slot(key)
        if i == None :
            return None
        if self.keys[i] != None:
            self.values[i] = value
        else:
            self.keys[i] = key
            self.values[i] = value
            #self.items += 1
        return key


    def hash_function(self, key):
        return key % self.size

    def remove(self, key):
        i = self.find_slot(key)
        if i == None:
          return None
        #i = self.find_slot(key)
        if self.keys[i] == None:
            return None
        j = i
        while True:
            self.keys[i] = None
            while True:
                j = (j+1) % self.size
                if self.keys[j] == None: # 이동 완료
                    return key

                k = self.hash_function(self.keys[j])
                if not (i < k <= j or j < i <k or k <=j < i):
                    break
            self.keys[i] = self.keys[j]
            self.values[i] = self.keys[j]
            i = j

    def search(self, key): # 탐색 - 완료
        i = self.find_slot(key)
        #print (i)
        if i != None and self.keys[i] != None:
            return self.keys[i]
        else:
            return None


    def __getitem__(self, key):
        return self.search(key)
    def __setitem__(self, key, value):
        self.set(key, value)

H = HashOpenAddr()
while True:
    cmd = input().split()
    if cmd[0] == 'set':
        key = H.set(int(cmd[1]))
        if key == None: print("* H is full!")
        else: print("+ {0} is set into H".format(cmd[1]))
    elif cmd[0] == 'search':
        key = H.search(int(cmd[1]))
        if key == None: print("* {0} is not found!".format(cmd[1]))
        else: print(" * {0} is found!".format(cmd[1]))
    elif cmd[0] == 'remove':
        key = H.remove(int(cmd[1]))
        if key == None:
            print("- {0} is not found, so nothing happens".format(cmd[1]))
        else:
            print("- {0} is removed".format(cmd[1]))
    elif cmd[0] == 'print':
        print(H)
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")