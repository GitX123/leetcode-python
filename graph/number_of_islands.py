"""
LeetCode 200

Tips:
* Search the entire island and sink the land by marking island as water
* Loop through all cells, and if '1' is found
    1. Sink the island using DFS
    2. Increment island count with 1.
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n_island = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # sink island by turning '1' to '0'
        def dfs(row, col):
            # boundary conditions
            if (
                row < 0 or
                row >= ROWS or
                col < 0 or
                col >= COLS or
                grid[row][col] == '0'
            ):
                return

            grid[row][col] = '0'
            for d_row, d_col in directions:
                dfs(row + d_row, col + d_col)


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1':
                    dfs(row, col)
                    n_island += 1

        return n_island