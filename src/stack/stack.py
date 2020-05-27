class Stack():
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty."

        data = self.stack.pop()
        print(data, " poped from stack")

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def peek(self):
        return self.stack[-1]

    def printStack(self):
        print(self.stack)
        
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)

    s.printStack()
    s.pop()
    s.printStack()
    print(s.peek())
    
