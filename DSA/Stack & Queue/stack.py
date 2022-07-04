from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
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




if __name__ == '__main__':
    s = Stack()
    s.push(5)
    print(s)
    print(s.is_empty())
    print(s.pop())
    print(s.is_empty())
    s.push(9)
    s.push(34)
    s.push(78)
    s.push(12)
    print(s)
    print(s.peek())