class Solution:
    """
    First and brute force solution
    """

    def isValid(self, s: str) -> bool:

        if not s or len(s) % 2 == 1:
            return False

        open_to_close_map = {'{': '}', '(': ')', '[': ']'}

        if s[0] not in open_to_close_map:
            return False

        stack = [s[0]]

        for x in s[1:]:
            if x in open_to_close_map:
                stack.append(x)

            else:
                if stack and open_to_close_map[stack[-1]] == x:
                    stack.pop()

                else:
                    return False

        return False if stack else True


class Solution:
    """
    Second and better solution.
    """
    def isValid(self, s: str) -> bool:

        stack = []
        close_to_open_map = {')': '(', '}': '{', ']': '['}

        if not s or len(s) % 2 == 1 or s[0] in close_to_open_map:
            return False

        for x in s:
            if x in close_to_open_map:
                if stack and stack[-1] == close_to_open_map[x]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(x)

        return True if not stack else False
