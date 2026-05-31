"""
LeetCode 230

Tips:
* Traverse the tree with inorder traversal using DFS

"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0 # tree pointer
        stack = []

        node = root
        while node or stack:
            # to left (dfs)
            while node:
                stack.append(node)
                node = node.left

            # pop if null
            node = stack.pop()
            n += 1
            if n == k:
                return node.val

            # to right
            node = node.right  