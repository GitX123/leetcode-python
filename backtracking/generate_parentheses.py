from typing import List

'''
Elements we need:
1. A recursive function to do backtracking
2. A stack to store parentheses

There are n open parentheses and close parenthese.
When adding a new parenthesis to a string, there must be more open parentheses than close parenthese (A parentheses
starts with open parenthesis),

Therefore,
1. open parentheses count < n && close parenthese count < n
2. open parentheses count > close parenthese count
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def backtrack(n_open, n_close):
            # base case
            if (n_open == n) and (n_close == n):
                result.append("".join(stack))
                return

            # recursive case
            if n_open < n:
                stack.append("(")
                backtrack(n_open + 1, n_close)
                stack.pop()

            if n_open > n_close:
                stack.append(")")
                backtrack(n_open, n_close + 1)
                stack.pop()

        backtrack(0, 0)
        return result