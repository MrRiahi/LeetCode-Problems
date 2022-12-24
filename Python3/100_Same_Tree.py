from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    This is my brute-force solution. It uses the iteration technique.
    Time complexity: O(len(p) + len(q))
    Space complexity: O(len(p) + len(q))
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


class Solution:
    """
    This is the more efficient solution. It uses the recursive technique.
    Time complexity: O(len(p) + len(q))
    Space complexity: O(len(p) + len(q))
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        left_flag = self.isSameTree(p=p.left, q=q.left)
        right_flag = self.isSameTree(p=p.right, q=q.right)

        return left_flag and right_flag
