class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0


def get_token_list(expr):
    token_list = []
    newExpr = expr.replace(" ", "")
    i = 0
    while i < len(newExpr):
        sum = newExpr[i]
        n = 1
        if '0' <= newExpr[i] <= '9':
            #print(newExpr[i])
            # sum = newExpr[i]
            if not (i == len(newExpr)-1) :
                if '0' <= newExpr[i + n] <= '9' or newExpr[i + n] == '.':
                    while '0' <= newExpr[i + n] <= '9' or newExpr[i + n] == '.':
                        sum += newExpr[i + n]
                        n += 1
                        #if (not ('0' <= newExpr[i + n] <= '9')) or not newExpr[i + n] == '.':
                         #   break
                        if i + n == len(newExpr):
                            break
                    i += n
                    #sum = float(sum)
                    token_list.append(sum)

                else:
                    #sum = float(sum)
                    token_list.append(sum)
                    i += 1
            else:
                #sum = float(sum)
                token_list.append(sum)
                i += 1
        else:
            token_list.append(sum)
            i += 1
    return token_list


def infix_to_postfix(token_list):
    opstack = Stack()
    outstack = []

    prec = {}
    prec['('] = 0
    prec['+'] = 1
    prec['-'] = 1
    prec['*'] = 2
    prec['/'] = 2
    prec['^'] = 3

    for token in token_list:
        # if 0<= token <= 999999:
        #   outstack.append(token)
        if token == '(':
            opstack.push(token)

        elif token == ')':
            while opstack.top() != '(':
                outstack.append(opstack.pop())
            if opstack.top() == '(':
                opstack.pop()

        elif token == '+' or token == '-' or token == '/' or token == '*' or token == '^':
            if not opstack.isEmpty():
                if opstack.top() == '(':
                    opstack.push(token)
                else:
                    while prec[token] <= prec[opstack.top()]:
                        outstack.append(opstack.pop())
                        if opstack.isEmpty(): break
                    opstack.push(token)
            else:
                opstack.push(token)
        else:  # operand일 때
            outstack.append(token)

    # opstack 에 남은 모든 연산자를 pop 후 outstack에 append
    if not opstack.isEmpty():
        while not opstack.isEmpty():
            outstack.append(opstack.pop())

    # return " ".join(outstack)
    return outstack


def compute_postfix(token_list):
    S = Stack()

    for token in token_list:
        if token == '+' or token == '-' or token == '*' or token == '/' or token == '^':
            a = S.pop()
            a = float(a)
            b = S.pop()
            b = float(b)
            if token == '+':
                S.push(a + b)
            elif token == '-':
                S.push(b - a)
            elif token == '*':
                S.push(a * b)
            elif token == '^':
                a = float(a)
                b = float(b)
                S.push(pow(b,a))
            else:
                S.push(b / a)
        else:
            S.push(token)
    return S.top()


# 아래 세 줄은 수정하지 말 것!
expr = input()
value = compute_postfix(infix_to_postfix(get_token_list(expr)))
print(value)