from collections import deque

class Stack:
    def __init__(self):
        self.container= deque()
    def push(self,val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container)
    def printstack(self):
        for i in range(self.size()):
            print(self.container[i])

s= Stack()
s.push(5)
s.push(10)
s.push(7)
s.push(8)
print(s.pop())
print(s.peek())
print(s.is_empty())
print(s.size())
print(s)
s.printstack()