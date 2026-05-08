'''
Requirement: all operations should be of constant time.

Trick:
1. Add a extra min stack to store min values start from each position (bottom to top) 
of the original stack.
2. The min value can be retrieved by simply looking at the top of the min stack.
3. When pushing to the original stack, compare it to the top and store the smaller one.
4. When poping from the original stack, we should also pop from the min stack.
'''
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
            return
        self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]