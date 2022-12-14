from typing import List


class Solution:
    """
    This is brute-force solution. It is not a time efficient solution. It has O(i*n) time complexity.
    """
    def pivotIndex(self, nums: List[int]) -> int:

        pivot_index = -1

        for i in range(len(nums)):
            left_sum = sum(nums[:i])
            right_sum = sum(nums[i + 1:])

            if left_sum == right_sum:
                pivot_index = i
                break

        return pivot_index


class Solution:
    """
    This is my second solution. It is more time efficient solution. It has O(n) time complexity.
    """
    def pivotIndex(self, nums: List[int]) -> int:

        pivot_index = -1
        right_sum = sum(nums[1:])
        left_sum = 0

        if right_sum == left_sum:
            pivot_index = 0
            return pivot_index

        for i in range(1, len(nums)):
            right_sum -= nums[i]
            left_sum += nums[i - 1]

            if left_sum == right_sum:
                pivot_index = i
                break

        return pivot_index


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        pivot_index = -1
        total = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            right_sum = total - nums[i] - left_sum

            if left_sum == right_sum:
                pivot_index = i
                break

            left_sum += nums[i]

        return pivot_index