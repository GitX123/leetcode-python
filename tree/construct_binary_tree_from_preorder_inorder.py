"""
LeetCode 105

Tips:
* The first node of the preorder list is the root node.
* The inorder will always go to the left, so the node from preorder corresponding to the node
  in inorder that splits the tree to the left and right subtree.
"""


from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Recursive DFS

Time Complexity: O(n^2)
Space Complexity: O(n)
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or inorder:
            return None
        
        # first node of preorder is the root
        root = TreeNode(preorder[0])

        # find the position correspoding to the inorder
        mid = inorder.index(preorder[0])

        # build left and right subtree from the root nodes
        root.left = self.buildTree(preorder[1: mid + 1], inorder[: mid])   # left subtree
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])     # right subtree
        return root