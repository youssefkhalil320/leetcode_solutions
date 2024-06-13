class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for idx in range(len(columnTitle) - 1, -1, -1):
            result += ((ord(columnTitle[idx]) - 65) + 1) * \
                (26 ** (len(columnTitle) - idx - 1))

        return result
