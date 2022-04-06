class Solution:
    def search(self, nums, target):
        """
        Implementation of the binary search method
        :param nums: List of sorted numbers
        :param target: Integer value
        :return:
        """

        if nums[0] > target or nums[-1] < target:
            return -1

        start_index = 0
        end_index = len(nums) - 1

        while start_index <= end_index:

            # This line is the simplification of the start_index + (end_index - start_index) // 2
            pivot = (end_index + start_index) // 2

            if nums[pivot] == target:
                return pivot

            elif nums[pivot] > target:
                end_index = pivot - 1

            else:
                start_index = pivot + 1

        return -1
