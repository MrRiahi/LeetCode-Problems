class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        digits = []
        while x >= 10:
            # Find the remainder of x divided by 10
            digit = x % 10

            # append the digit to a list
            digits.append(digit)

            # Find the quotient
            x = x // 10

        digits.append(x)

        if digits == digits[::-1]:
            return True

        return False
