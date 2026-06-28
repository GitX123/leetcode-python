'''
No. 15
Medium
'''

from typing import List

class Solution(object):
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        # sort input array
        nums.sort()

        # loop through a to find b, c
        for i, a in enumerate(nums):
            if a > 0:
                break
            
            # pass duplicates
            if i > 0 and a == nums[i-1]:
                continue

            # loop through b to find c
            for j, b in enumerate(nums[i+1:]):
                if a + b > 0:
                    break

                # pass duplicates
                if j > 0 and b == nums[j+i]:
                    continue

                c = -a - b
                if c in nums[j+i+2:]: # the in operator iterate over every element, which is slow in this case
                    result.append([a, b, c])

        return result
    
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        result = []

        # sort input array
        nums.sort()

        # loop through a to find b, c
        for i, a in enumerate(nums):
            if a > 0:
                break

            # pass duplicates
            if i > 0 and a == nums[i-1]:
                continue

            # use left/right pointers to find b, c
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = a + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1

                    # move l to the left if we have consecutive duplicates
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return result