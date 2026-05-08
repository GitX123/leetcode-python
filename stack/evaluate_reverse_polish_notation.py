'''
Elements we need
* Stack: to store numbers (from inputs and calculated results)

1. Go throught the inputs.
2. If it is a number, push it into stack.
3. If it is an operator, pop two numbers from stack and calculate.
4. Push the calculated result into stack.
5. After going throught all inputs, the result is placed at the top of the stack.
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            # operators
            if c == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(b + a)
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                a, b = stack.pop(), stack.pop()
                stack.append(b * a)
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            # numbers
            else:
                stack.append(int(c))

        return stack[-1]