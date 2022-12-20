class Solution:
    """
    This is my first solution.
    Time complexity: O(n)
    Space Complexity: O(1) or more specifically O(26)
    """
    def titleToNumber(self, columnTitle: str) -> int:

        alphabet = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
                    'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
                    'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
                    'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
                    'Z': 26}

        result = 0

        for i, char in enumerate(columnTitle[::-1]):
            result += (26 ** i) * alphabet[char]

        return result


class Solution:
    """
    This is my second solution.
    Time complexity: O(n)
    Space Complexity: O(1)
    """
    def titleToNumber(self, columnTitle: str) -> int:

        result = 0

        for i, char in enumerate(columnTitle[::-1]):
            result += (26 ** i) * (ord(char) - 64)

        return result
