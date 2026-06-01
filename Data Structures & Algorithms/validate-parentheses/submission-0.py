class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top != dic[ch]:
                    return False
        return len(stack) == 0

        