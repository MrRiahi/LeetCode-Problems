class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        len_list = len(nums)

        if nums[0] > target or nums[0] == target:
            return 0

        if nums[-1] < target:
            return len_list

        if nums[-1] == target:
            return len_list - 1

        start_index = 0
        stop_index = len_list - 1

        while start_index <= stop_index:

            pivot = (start_index + stop_index) // 2

            if nums[pivot] == target:
                return pivot

            elif nums[pivot] < target:
                start_index = pivot + 1

            elif nums[pivot] > target:
                stop_index = pivot - 1

        return start_index
