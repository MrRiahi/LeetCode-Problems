from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l_pointer = 0

        for r_pointer in range(len(nums)):
            if nums[r_pointer] != val:
                nums[l_pointer] = nums[r_pointer]
                l_pointer += 1

        return l_pointer
