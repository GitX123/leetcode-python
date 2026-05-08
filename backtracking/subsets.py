from typing import List

'''
Tips:
1. One path to include nothing.
2. One path to include current element.

Ref:
https://youtu.be/L0NxT2i-LOY?si=3X-ehekSp9-3CRwP
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def backtrack(i, subset: List[int]):
            # base condition
            if i >= n:
                result.append(subset.copy())
                return
            
            # include nothing and go to next
            backtrack(i + 1, subset)

            # include current element and go to next
            subset.append(nums[i])
            backtrack(i + 1, subset)

            # backtrack before we go back to upper level
            subset.pop()

        backtrack(0, [])
        return result