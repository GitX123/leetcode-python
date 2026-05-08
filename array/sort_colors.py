'''
No. 75
Medium
'''
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, r = 0, len(nums) - 1 # left and right pointer

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        i = 0
        while i <= r:
            if nums[i] == 0:
                # move to left partition
                swap(i, l)
                l += 1
            elif nums[i] == 2:
                # move to right partition
                swap(i, r)
                r -= 1
                i -= 1 # check again
            i += 1