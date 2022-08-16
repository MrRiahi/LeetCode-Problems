class Solution1:
    def lengthOfLastWord(self, s: str) -> int:
        """
        First solution.
        :param s: 
        :return: 
        """""
        words = s.split(' ')

        if len(words) == 1:
            return len(words[0])

        for i in range(len(words) - 1, -1, -1):
            if len(words[i]) != 0:
                return len(words[i])


class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Second solution.
        :param s:
        :return:
        """

        return len(s.rstrip().split(' ')[-1])
