from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    This my first recursive solution.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        # Base case
        if not root:
            return result

        if not root.left and not root.right:
            result.append(root.val)
            return result

        # recursive case
        left_val = self.postorderTraversal(root.left)  # go to left part of tree
        right_val = self.postorderTraversal(root.right)  # go to right part of tree

        result.extend([*left_val, *right_val, root.val])

        return result


class Solution:
    """
    This my second recursive solution.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        if root:
            left_results = self.postorderTraversal(root.left)
            right_results = self.postorderTraversal(root.right)

            result.extend(left_results)
            result.extend(right_results)
            result.append(root.val)

        return result


class Solution:
    """
    This the third and iterative solution.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return result[::-1]