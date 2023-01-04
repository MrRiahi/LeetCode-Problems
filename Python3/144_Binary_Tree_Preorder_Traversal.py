from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    This is my first solution. It is a recursive one.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        if root:
            result.append(root.val)
            result.extend(self.preorderTraversal(root=root.left))
            result.extend(self.preorderTraversal(root=root.right))

        return result


class Solution:
    """
    This is my second solution. It is a recursive one.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        # Base case
        if not root:
            return []

        # recursive case
        result.append(root.val)
        result.extend([*self.preorderTraversal(root=root.left),
                       *self.preorderTraversal(root=root.right)])

        return result


class Solution:
    """
    This is my third solution. It is an iterative one.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # Base case
        if not root:
            return []

        result = []
        cur_node = root
        stack = []

        while stack or cur_node:
            while cur_node:
                result.append(cur_node.val)
                stack.append(cur_node)
                cur_node = cur_node.left

            cur_node = stack.pop()
            cur_node = cur_node.right

        return result