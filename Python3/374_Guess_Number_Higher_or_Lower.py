# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

"""
In this problem, I use Ternary Search. I select mid1 and mid2 points and get the results for these points
named guess_result1 and guess_result2, respectively. It is obvious that the guess_result1=-1 and
guess_result2=1 is an invalid state. Therefore, there are 3 other states. If the guess_result1=guess_result2=-1
(in abstract guess_result1=-1), I change the high to mid1 - 1. If the guess_result1=guess_result2=1
(in abstract guess_result2=1), I change the low to mid2 + 1. If guess_result1=1 and guess_result2=-1, the high
is mid2 - 1 and low is mid1 + 1
"""


class Solution:
    def guessNumber(self, n: int) -> int:
        """
        Guess the number. The computer picks a number between 1 and n.
        :param n: maximum number
        :return:
        """

        low = 1
        high = n

        if n == 1:
            return 1

        while low <= high:

            mid1 = low + (high - low) // 3
            mid2 = high - (high - low) // 3

            guess_result1 = guess(mid1)
            guess_result2 = guess(mid2)

            if guess_result1 == 0:
                return mid1

            elif guess_result2 == 0:
                return mid2

            elif guess_result1 == -1:
                high = mid1 - 1

            elif guess_result2 == 1:
                low = mid2 + 1

            else:
                low = mid1 + 1
                high = mid2 - 1
