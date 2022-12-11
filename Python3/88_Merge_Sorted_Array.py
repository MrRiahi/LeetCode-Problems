from typing import List


class Solution:
    """
    This is the NeetCode solution
    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m + n - 1  # pointer on the whole nums1 array

        while n > 0 and m > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[p] = nums1[m - 1]
                m -= 1

            else:
                nums1[p] = nums2[n - 1]
                n -= 1

            p -= 1

        # Fill the nums1 array with the leftover nums2
        while n > 0:
            nums1[p] = nums2[n - 1]
            n -= 1
            p -= 1
