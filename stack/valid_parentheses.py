
'''
The first come parenthese has to matched last, vice versa.
This matches the FILO property implied by a stack.
1. Store encountered parenthese in stack.
2. Poped if matched parenthese is encountered.
3. If stack is empty in the end, then the it is valid.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheseMap = {')': '(', 
                         '}': '{', 
                         ']': '['}

        for c in s:
            if c in parentheseMap:
                if not stack or stack[-1] != parentheseMap[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)

        return (not stack)