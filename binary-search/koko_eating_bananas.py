from typing import List
import math

'''
Tips:
* The max speed would be max(piles), because Koko can finish any pile within an hour with this speed.
* The min speed is above 1.
* We can search the min speed within this range [1, max(piles)]

1. Look for min speed starts from 1 to max(piles).
2. Set left and right pointers to 1 and max(piles).
3. Loop until left and right pointer meets:
    a. Calculate time spent with the mid pointer.
    b. If time spent is valid:
        1. Record the mid value.
        2. Move right pointer to search for lower speed.
    c. If time spent is invalid:
        1. Move left pointer to search for higher value.
'''

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        speed = r
        
        while l <= r:
            m = l + (r - l) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile) / m)

            if hours <= h: # valid but look for lower speed
                speed = m
                r = m - 1
            else: # invalid and look for higher speed
                l = m + 1

        return speed