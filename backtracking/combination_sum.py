from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, combination: List[int], sum: int):
            # base condition
            if sum == target:
                result.append(combination.copy())
                return

            if i >= len(candidates) or sum > target:
                return

            # recursive condition
            combination.append(candidates[i])
            dfs(i, combination, sum + candidates[i])
            combination.pop()
            dfs(i + 1, combination, sum)

        dfs(0, [], 0)
        return result