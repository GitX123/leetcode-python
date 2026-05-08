from typing import List

'''
Tips
* When the nubmers are rotated, there are two ascending sorted portions: left and right
* Differentiate wether the mid pointer is in left or right sorted portions, because this affects
  how we move to left or right side when comparing mid pointer to the target.

1. Loop until left and right pointers cross:
    a. If mid pointer equals target, return mid pointer.
    b. If mid pointer is in left sorted portion:
        1. If target > mid -> move to right side.
        2. If target < mid and  target >= left -> move to left side.
        3. If target < mid and target < left move to right side
    c. If mid pointer is in right sorted portion:
        1. If target > mid and  target <= right -> move to right side.
        2. If target > mid and target > right -> move to left side
        3. If target < mid -> move to left side.
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if target == nums[m]:
                return m
            
            # left sorted portion
            if nums[m] > nums[r]:
                if target > nums[m]:
                    l = m + 1
                else:
                    if target >= nums[l]:
                        r = m -1
                    else:
                        l = m + 1
            # right sorted portion or not rotated
            else:
                if target > nums[m]:
                    if target <= nums[r]:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    r = m - 1

        return -1