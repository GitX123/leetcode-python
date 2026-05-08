from typing import List

'''
1. Create left and right pointers.
2. Loop until left pointer cross right pointer:
    a. If mid pointer is bigger than the target, then search the left side by assigning 
       right pointer to mid pointer minus 1.
    b. If mid pointer is smaller than the target, then search the right side by assigning 
       left pointer to mid pointer plus 1.
    c. If mid pointer is equal to the target, return mid pointer.
3. Return -1 if no match found.
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] > target:
                r = m -1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
            
        return -1