from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    This is my first solution. It is a recursive depth first search approach.
    Time complexity: O(n)
    Space Complexity: O(1)
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        right_depth = self.maxDepth(root.right) + 1
        left_depth = self.maxDepth(root.left) + 1

        return max(right_depth, left_depth)


class Solution:
    """
    This is the second solution. It is an iterative breadth first search approach.
    Time complexity: O(n)
    Space Complexity: O(1)
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        level = 0
        q = deque([root])

        while q:

            len_level = len(q)
            for i in range(len_level):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1

        return level


class Solution:
    """
    This is the third solution. It is an iterative depth first search approach.
    Time complexity: O(n)
    Space Complexity: O(1)
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        nodes = [root]
        depth = [1]
        max_depth = 1

        while nodes:
            cur_node = nodes.pop()
            cur_depth = depth.pop()

            if cur_node.left:
                nodes.append(cur_node.left)
                depth.append(cur_depth + 1)

            if cur_node.right:
                nodes.append(cur_node.right)
                depth.append(cur_depth + 1)

            max_depth = max(cur_depth, max_depth)

        return max_depth


class Solution:
    """
    This is the fourth solution. It is an iterative depth first search approach which much cleaner.
    Time complexity: O(n)
    Space Complexity: O(1)
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        stack = [[root, 1]]
        max_depth = 0

        while stack:
            node, depth = stack.pop()

            if node:
                max_depth = max(depth, max_depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return max_depth
