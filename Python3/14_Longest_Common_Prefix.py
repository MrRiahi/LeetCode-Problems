from typing import List


class Solution:
    """
    First solution
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""

        for i, letter in enumerate(strs[0]):
            for item in strs[1:]:
                if i >= len(item) or letter != item[i]:
                    return common_prefix

            common_prefix += letter

        return common_prefix
