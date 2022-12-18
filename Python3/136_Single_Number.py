from typing import List


class Solution:
    """
    This is my first solution. It has O(2*n) time complexity and O(n) memory complexity.
    """
    def singleNumber(self, nums: List[int]) -> int:

        data_counter = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in data_counter:
                data_counter[num] += 1
            else:
                data_counter[num] = 1

        for num in data_counter:
            if data_counter[num] == 1:
                return num


class Solution:
    """
    This is my second solution. It has O(n) time complexity and O(n) memory complexity.
    """
    def singleNumber(self, nums: List[int]) -> int:

        data_counter = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in data_counter:
                del data_counter[num]
            else:
                data_counter[num] = 1

        return list(data_counter.keys())[0]


class Solution:
    """
    This is the non-trivial answer from NeetCode. It uses the XOR concept.
    It has O(n) time complexity and O(1) memory complexity.
    """
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for i in nums:
            result = i ^ result

        return result
