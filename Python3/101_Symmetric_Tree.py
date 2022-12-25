from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    """
    This is my first solution. It uses the iteration technique.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root.left and not root.right:
            return True

        if not root.left or not root.right:
            return False

        right = [root.right]
        left = [root.left]

        while right or left:
            node_r = right.pop()
            node_l = left.pop()
            if node_r.val != node_l.val:
                return False

            if (node_r.right and not node_l.left) or (not node_r.right and node_l.left):
                return False

            if (node_r.left and not node_l.right) or (not node_r.left and node_l.right):
                return False

            if node_r.right and node_l.left:
                right.append(node_r.right)
                left.append(node_l.left)

            if node_r.left and node_l.right:
                right.append(node_r.left)
                left.append(node_l.right)

        return True


class Solution2:
    """
    This is my second solution. It is not a clear code.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        return self.isMirror(root.left, root.right)

    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]):

        if not left and not right:
            return True

        if not left or not right:
            return False

        if left.right and right.left:
            result_1 = self.isMirror(left=left.right, right=right.left)

        elif left.right and not right.left:
            result_1 = False

        elif not left.right and right.left:
            result_1 = False

        else:
            result_1 = True

        if left.left and right.right:
            result_2 = self.isMirror(left=left.left, right=right.right)

        elif left.left and not right.right:
            result_2 = False

        elif not left.left and right.right:
            result_2 = False

        else:
            result_2 = True

        return result_1 and result_2 and (left.val == right.val)


class Solution3:
    """
    This is mt third solution. It is the updated version of the Solution2.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        return self.isMirror(left=root, right=root)

    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]):

        if not left and not right:
            return True

        elif not left or not right:
            return False

        else:
            result_1 = self.isMirror(left=left.right, right=right.left)
            result_2 = self.isMirror(left=left.left, right=right.right)

            return result_1 and result_2 and (left.val == right.val)


class Solution4:
    """
    This is the third solution. It is clean and readable.
    Time complexity: O(n)
    Space complexity: O(n)
    """

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        return self.isMirror(left=root, right=root)

    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]):

        if not left and not right:
            return True

        elif not left or not right:
            return False

        else:
            result_1 = self.isMirror(left=left.left, right=right.right)
            result_2 = self.isMirror(left=left.right, right=right.left)

            return (left.val == right.val) and result_1 and result_2
