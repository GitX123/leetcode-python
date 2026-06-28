'''
No. 11
Medium
'''

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        p_l, p_r = 0, len(height) - 1 # left and right pointer

        while p_l != p_r:
            # calculate area
            area = (p_r - p_l) * min(height[p_l], height[p_r])
            max_area = max_area if (max_area > area) else area

            # move the pointer
            if height[p_l] > height[p_r]:
                p_r -= 1
            elif height[p_l] < height[p_r]:
                p_l += 1
            else:
                p_r -= 1
        
        return max_area
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea([1,8,6,2,5,4,8,3,7]))