from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    This is my first solution. This is the recursive solution.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        if root:
            left_results = self.inorderTraversal(root.left)
            right_results = self.inorderTraversal(root.right)

            result.extend(left_results)
            result.append(root.val)
            result.extend(right_results)

        return result


class Solution:
    """
    This is the iterative solution.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []
        stack = []
        pointer = root

        while pointer or stack:
            while pointer:
                stack.append(pointer)
                pointer = pointer.left

            pointer = stack.pop()
            result.append(pointer.val)
            pointer = pointer.right

        return result
