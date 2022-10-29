class Solution:
    """
    First solution
    """

    def __init__(self):
        self.symbol_to_value = {'I': 1,
                                'V': 5,
                                'X': 10,
                                'L': 50,
                                'C': 100,
                                'D': 500,
                                'M': 1000,
                                }

    def romanToInt(self, s: str) -> int:

        state_0 = 'M'
        roman_num = 0
        for state_1 in s:
            if self.symbol_to_value[state_1] <= self.symbol_to_value[state_0]:
                roman_num += self.symbol_to_value[state_1]
                state_0 = state_1

            else:
                roman_num += (self.symbol_to_value[state_1] - 2 * self.symbol_to_value[state_0])
                state_0 = state_1

        return roman_num


class Solution:
    """
    Second solution
    """
    def __init__(self):
        self.symbol_to_value = {'I': 1,
                                'V': 5,
                                'X': 10,
                                'L': 50,
                                'C': 100,
                                'D': 500,
                                'M': 1000,
                                }

    def romanToInt(self, s: str) -> int:
        state_0 = s[0]
        roman_num = 0

        if len(s) == 1:
            roman_num += self.symbol_to_value[state_0]
            return roman_num

        for state_1 in s[1:]:
            if self.symbol_to_value[state_1] <= self.symbol_to_value[state_0]:
                roman_num += self.symbol_to_value[state_0]
                state_0 = state_1

            else:
                roman_num -= self.symbol_to_value[state_0]
                state_0 = state_1

        roman_num += self.symbol_to_value[s[-1]]

        return roman_num


class Solution:
    """
    Third solution
    """
    def __init__(self):
        self.symbol_to_value = {'I': 1,
                                'V': 5,
                                'X': 10,
                                'L': 50,
                                'C': 100,
                                'D': 500,
                                'M': 1000,
                                }

    def romanToInt(self, s: str) -> int:
        roman_num = 0

        for i in range(len(s)):
            if (i + 1) < len(s) and self.symbol_to_value[s[i]] < self.symbol_to_value[s[i + 1]]:
                roman_num -= self.symbol_to_value[s[i]]
            else:
                roman_num += self.symbol_to_value[s[i]]

        return roman_num