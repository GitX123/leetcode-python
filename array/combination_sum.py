'''
No. 39
Medium
'''

from typing import List

class Solution(object):
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result_arr = []
        

        ''' 
        depth first search function looking for qualified combination
        - i: index of candidates
        - current_comb: placeholder for current combination
        - sum: sum of current combination
        '''
        def dfs_comb(i, current_comb, sum):
            if sum == target:
                result_arr.append(current_comb.copy())
                return
            if i >= len(candidates) or sum > target:
                return
            
            # search recursively
            current_comb.append(candidates[i])
            dfs_comb(i, current_comb, sum + candidates[i])
            current_comb.pop()
            dfs_comb(i + 1, current_comb, sum)

        dfs_comb(0, [], 0)
        return result_arr