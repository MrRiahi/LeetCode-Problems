class Solution:
    """
    My solution
    """

    def addBinary(self, a: str, b: str) -> str:

        if len(a) < len(b):
            a = (len(b) - len(a)) * '0' + a

        if len(b) < len(a):
            b = (len(a) - len(b)) * '0' + b

        overflow = 0
        result = ''

        for i, j in zip(a[::-1], b[::-1]):
            if i == '0' and j == '0':
                if overflow == 0:
                    result = '0' + result
                else:
                    result = '1' + result

                overflow = 0

            elif ((i == '1' and j == '0') or (i == '0' and j == '1')):
                if overflow == 0:
                    result = '1' + result
                    overflow = 0
                else:
                    result = '0' + result
                    overflow = 1

            else:
                if overflow == 0:
                    result = '0' + result
                else:
                    result = '1' + result

                overflow = 1

        if overflow == 1:
            result = '1' + result

        return result


class Solution:
    """
    NeetCode solution
    """

    def addBinary(self, a: str, b: str) -> str:

        result = ''
        overflow = 0

        a = a[::-1]
        b = b[::-1]

        for i in range(max(len(a), len(b))):
            digit_a = ord(a[i]) - ord('0') if i < len(a) else 0
            digit_b = ord(b[i]) - ord('0') if i < len(b) else 0

            total = digit_a + digit_b + overflow
            result = str(total % 2) + result
            overflow = total // 2

        if overflow:
            result = '1' + result

        return result