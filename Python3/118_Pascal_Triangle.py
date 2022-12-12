from typing import List


class Solution:
    """
    This is my first solution. It has O(numRows ^ 2) time complexity and O(2n) memory complexity
    """
    def generate(self, numRows: int) -> List[List[int]]:

        result = [[1]]

        for i in range(1, numRows):
            new_row = [1]
            print(f'i is {i}, result is {result}')
            for j in range(i - 1):
                item = result[i - 1][j] + result[i - 1][j + 1]
                new_row.append(item)

            new_row.append(1)
            result.append(new_row)

        return result


class Solution:
    """
    This is my second solution. It has O(numRows ^ 2) time complexity and O(n) memory complexity.
    This solution is more efficient in memory complexity.
    """
    def generate(self, numRows: int) -> List[List[int]]:

        result = [[1]]

        for i in range(1, numRows):
            result.append([1])
            for j in range(i - 1):
                item = result[i - 1][j] + result[i - 1][j + 1]
                result[i].append(item)

            result[i].append(1)

        return result


class Solution:
    """
    This is the NeetCode solution.
    """
    def generate(self, numRows: int) -> List[List[int]]:

        result = [[1]]

        for i in range(numRows - 1):
            temp = [0] + result[-1] + [0]
            row = []
            for j in range(len(result[-1]) + 1):
                row.append(temp[j] + temp[j + 1])

            result.append(row)

        return result
