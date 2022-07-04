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

def reverse_string(s):
    stack = Stack()

    for ch in s:
        stack.push(ch)

    result = ''
    while stack.size()!=0:
        result += stack.pop()
    
    return result

def is_match(ch1,ch2):
    match_dict = {
        ')':'(',
        ']':'[',
        '}':'{'
    }
    return match_dict[ch1] == ch2

def is_balanced(s):
    stack = Stack()

    for ch in s:
        if ch == '(' or ch == '{' or ch == '[':
            stack.push(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if stack.size() == 0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    
    return stack.size() == 0
 



if __name__ == '__main__':
    s = Stack()
    # s.push(5)
    # # print(s)
    # print(s.is_empty())
    # print(s.pop())
    # print(s.is_empty())
    # s.push(9)
    # s.push(34)
    # s.push(78)
    # s.push(12)
    # # print(s)
    # print(s.peek())
    # print(reverse_string('We will conquere COVI-19'))
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))

