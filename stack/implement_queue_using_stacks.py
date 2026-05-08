
'''
Elements we need:
* Two stacks: one for storing incoming pushed data, the other to reverse the order of the first 
stack, so we have a FIFO structure.
'''
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    '''
    1. If stack2 is empty, push all elements from stack1 to stack2
    2. Pop from stack2
    '''
    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()
        
    '''
    The same as pop operation, but only return the element.
    '''
    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]      
        
    '''
    The queue is empty if both stacks are empty
    '''
    def empty(self) -> bool:
        return max(len(self.stack1), len(self.stack2)) == 0