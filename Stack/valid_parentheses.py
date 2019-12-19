class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ['(', '{', '[']
        close_brackets = [')', '}', ']']

        stack = []

        for c in s:
            if c in open_brackets:
                stack.append(c)
            elif c in close_brackets:
                pos = close_brackets.index(c)
                if stack and stack[-1] == open_brackets[pos]:
                    stack.pop()
                else:
                    return False

        if not stack:
            return True