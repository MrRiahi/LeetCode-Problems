class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        count = 0
        arr2.sort()
        arr2_len = len(arr2)
        for x in arr1:
            index = bisect.bisect_left(arr2, x)
            min_dist = float('inf')

            if index > 0:
                min_dist = min(min_dist, abs(x - arr2[index - 1]))
            if index < arr2_len:
                min_dist = min(min_dist, abs(x - arr2[index]))

            if min_dist > d:
                count += 1

        return count
