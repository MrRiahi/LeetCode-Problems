from typing import List


class Solution:
    """
    This is my brute-force solution. Memory complexity is O(n)
    """
    def runningSum(self, nums: List[int]) -> List[int]:

        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(nums[0])
            else:
                num = nums[i] + result[-1]
                result.append(num)

        return result


class Solution:
    """
    This is second solution. It more memory efficient (O(1)).
    """
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        return nums
