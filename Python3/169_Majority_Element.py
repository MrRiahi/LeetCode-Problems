from typing import List

class Solution:
    """
    This is my brute-force solution.
    Time complexity: O(n + m) where n is len(nums) and m is len(iter_dict)
    Space complexity: O(n)
    """
    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums)

        # Base case
        if n == 1:
            return nums[0]

        iter_dict = {}
        for num in nums:
            if num in iter_dict:
                iter_dict[num] += 1
            else:
                iter_dict[num] = 0

        return max(iter_dict, key=lambda x: iter_dict[x])


class Solution:
    """
    This is my second solution. It is the improved version of the previous one.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums)

        # Base case
        if n == 1:
            return nums[0]

        iter_dict = {}
        for num in nums:
            if num in iter_dict:
                iter_dict[num] += 1
                if iter_dict[num] >= (n // 2):
                    return num
            else:
                iter_dict[num] = 0


class Solution:
    """
    This is the NeetCode solution. It uses the Boyer-Moore technique to optimize memory complexity.
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums)

        # Base case
        if n == 1:
            return nums[0]

        result = 0
        count = 0

        for num in nums:
            if count == 0:
                result = num
            count += 1 if num == result else -1

        return result
