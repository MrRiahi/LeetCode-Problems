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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Base case
        if len(nums) == 0:
            return None

        # Create root
        root_index = len(nums) // 2
        root = TreeNode(val=nums[root_index])
        
        ## Recursive case
        root.left = self.sortedArrayToBST(nums=nums[:root_index])
        root.right = self.sortedArrayToBST(nums=nums[root_index + 1:])
        
        return root


class Solution:
    """
    This is the second solution from NeetCode. It is a recursive one.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def helper(l_index, r_index):
            if l_index > r_index:
                return None

            root_index = (l_index + r_index) // 2
            root = TreeNode(val=nums[root_index])
            root.left = helper(l_index=l_index, r_index=root_index-1)
            root.right = helper(l_index=root_index+1, r_index=r_index)

            return root
        
        tree = helper(l_index=0, r_index=len(nums)-1)

        return tree