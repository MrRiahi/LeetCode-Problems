class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        if len(arr) == 3:
            return 1

        start_index = 0
        stop_index = len(arr) - 1

        while start_index < stop_index:

            pivot = (start_index + stop_index) // 2

            if arr[pivot] > arr[pivot - 1] and arr[pivot] > arr[pivot + 1]:
                return pivot

            elif arr[pivot] < arr[pivot + 1]:
                start_index = pivot + 1

            elif arr[pivot] < arr[pivot - 1]:
                stop_index = pivot
