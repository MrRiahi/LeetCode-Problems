from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    This is my brute-force solution.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        stack_p = [p]
        stack_q = [q]

        while stack_p and stack_p:
            cur_p = stack_p.pop()
            cur_q = stack_q.pop()

            if cur_p.val != cur_q.val:
                return False

            if cur_p.left and cur_q.left:
                stack_p.append(cur_p.left)
                stack_q.append(cur_q.left)

            if (cur_p.left and not cur_q.left) or (not cur_p.left and cur_q.left):
                return False

            if cur_p.right and cur_q.right:
                stack_p.append(cur_p.right)
                stack_q.append(cur_q.right)

            if (cur_p.right and not cur_q.right) or (not cur_p.right and cur_q.right):
                return False

        return True







