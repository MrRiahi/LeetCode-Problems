from typing import List


class Solution:
    """
    This is my brute-force solution.
    Time complexity: O(nxm)
    Space complexity: O(n or m)
    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        result = []
        if not nums1 or not nums2:
            return result

        for i in nums1:
            if i in nums2 and i not in result:
                result.append(i)

        return result


class Solution:
    """
    This is my second solution.
    Time complexity: O(n + m)
    Space complexity: O(n or m)
    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        result = []
        if not nums1 or not nums2:
            return result

        nums2_dict = {}
        for i in nums2:
            if i not in nums2_dict:
                nums2_dict[i] = True

        for i in nums1:
            if i in nums2_dict and i not in result:
                result.append(i)

        return result


class Solution:
    """
    This is my third and most efficient solution.
    Time complexity: O(n + m)
    Space complexity: O(n or m)
    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        result = {}
        nums2_dict = {}

        if not nums1 or not nums2:
            return result

        for i in nums2:
            if i not in nums2_dict:
                nums2_dict[i] = True

        for i in nums1:
            if i in nums2_dict and i not in result:
                result[i] = True

        return result
