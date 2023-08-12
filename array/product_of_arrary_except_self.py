'''
No. 238
Medium
'''

from typing import List

class Solution(object):
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result_arr = [1] * len(nums)

        # store prefixes into result array
        prefix = 1
        for i in range(len(result_arr)):
            result_arr[i] = prefix
            prefix *= nums[i]

        # multiply postfixes to get the right values
        postfix = 1
        for i in range(len(result_arr) - 1, -1, -1):
            result_arr[i] *= postfix
            postfix *= nums[i]

        return result_arr