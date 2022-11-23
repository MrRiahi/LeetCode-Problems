class Solution:
    """
    My solution.
    It is top to bottom approach
    """

    def climbStairs(self, n: int) -> int:

        cache = {1: 1, 2: 2}

        if n in cache:
            return cache[n]

        cnt = 3
        while cnt < n:
            cache[cnt] = cache[cnt - 1] + cache[cnt - 2]
            cnt += 1

        return cache[cnt - 1] + cache[cnt - 2]


class Solution:
    """
    NeetCode solution.
    It is bottom up approach.
    """

    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1

        for _ in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one
