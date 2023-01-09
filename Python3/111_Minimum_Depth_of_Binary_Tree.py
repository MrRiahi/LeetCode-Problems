from collections import deque
from typing import Optional
from math import inf

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    This is my first solution. It is iterative depth first search.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def minDepth(self, root: Optional[TreeNode]) -> int:

        min_depth = inf

        # Base case
        if not root:
            return 0

        stack = []
        depth = 0
        cur_node = root

        while stack or cur_node:
            while cur_node:
                depth += 1
                stack.append((cur_node, depth))
                cur_node = cur_node.left

            cur_node, depth = stack.pop()

            # Check whether it is a leaf or not
            if not cur_node.right and not cur_node.left:
                min_depth = min(min_depth, depth)

            cur_node = cur_node.right

        return min_depth


class Solution:
    """
    This is my second solution. It is recursive depth first search.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.min_depth = inf

        # Base case
        if not root:
            return 0

        # Recursive case
        self.depth_first_search(root, 1)

        return self.min_depth

    def depth_first_search(self, node, depth):
        if not node:
            return

        if not node.left and not node.right:
            self.min_depth = min(self.min_depth, depth)

        self.depth_first_search(node.left, depth + 1)
        self.depth_first_search(node.right, depth + 1)


class Solution:
    """
    This is my third solution. It is iterative breadth first search.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def minDepth(self, root: Optional[TreeNode]) -> int:

        min_depth = 0

        if not root:
            return min_depth

        que = deque([(root, 1)])

        while que:
            node, depth = que.popleft()

            if not node.left and not node.right:
                return depth

            if node.left:
                que.append((node.left, depth + 1))

            if node.right:
                que.append((node.right, depth + 1))

        return -1
