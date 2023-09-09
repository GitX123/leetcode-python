'''
No. 56
Easy
'''

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority, count = 0, 0
        '''
        - encounter the same number: count plus 1
        - encounter different number: count minus 1
        - change majority to num once count is 0
        '''
        for num in nums:
            if count == 0:
                majority = num
            count += (1 if num == majority else -1)

        return majority
