class Solution:
    def mySqrt(self, x: int) -> int:

        if x <= 1:
            return x

        low = 1
        high = x // 2

        while low <= high:

            mid = (low + high) // 2
            square = mid ** 2

            if square == x:
                return mid

            if square < x:
                low = mid + 1
            else:
                high = mid - 1

        return high
