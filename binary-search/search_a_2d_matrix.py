from typing import List

'''
1. Do binary search along the rows.
2. Do binary search along the cloumns

Time: O(long(m) + long(n))
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # binary search along the rows
        top, bottom = 0, ROWS - 1
        while top <= bottom:
            row = top + (bottom - top) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break

        # binary search along the cols
        l, r = 0, COLS - 1
        while l <= r:
            m = l + (r - l) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
            
        return False