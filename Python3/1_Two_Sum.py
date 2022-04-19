from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """
        This is my naive solution for two sum problem. It has O(n^2) time complexity.
        :param nums:
        :param target:
        :return:
        """

        result = []

        for i in nums:
            if target - i in nums:
                if target - i == i and nums.count(target - i) == 1:
                    continue

                first_index = nums.index(i)
                nums.remove(i)
                second_index = nums.index(target - i) + 1
                result = [first_index, second_index]
                break

        return result
