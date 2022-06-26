# p.241~ 9장
class Solution:
    # p.245 다시풀기
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for char in s:
            if char in table.keys():
                stack.append(char)
            elif not stack or table[stack.pop()] != char:
                return False
        return len(stack) == 0

    # p.247
    def removeDuplicateLetters(self, s: str) -> str:
        chars = ""
        for char in s:
            if char not in chars:
                chars += char
        return "".join(sorted(chars))

sol = Solution()
letters = sol.removeDuplicateLetters("cbacdcbc")
print(letters)
