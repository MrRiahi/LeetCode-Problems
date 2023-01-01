from typing import List

class Solution:
    """
    This is my first recursive solution.
    Time complexity: O(rowIndex)
    Space complexity: O(rowIndex)
    """
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1, 1]

        row = self.getRow(rowIndex=rowIndex - 1)

        result = [1] * (rowIndex + 1)
        for i in range(len(row) - 1):
            result.append(row[i] + row[i + 1])
        result.append(1)

        return result

class Solution:
    """
    This is my second recursive solution.
    Time complexity: O(4*rowIndex)
    Space complexity: O(rowIndex)
    """
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1, 1]

        row = self.getRow(rowIndex=rowIndex - 1)

        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]

        return row


class Solution:
    """
    This is my third recursive solution.
    Time complexity: O(rowIndex)
    Space complexity: O(rowIndex)
    """
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1, 1]

        row = self.getRow(rowIndex=rowIndex - 1)

        result = [1] * (rowIndex + 1)
        for i in range(1, len(row)):
            result[i] = row[i - 1] + row[i]

        return result