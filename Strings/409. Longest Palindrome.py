from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        fmap = Counter(s)
        res = 0
        hasOddFrequency = len(s) % 2 != 0
        for i in fmap:
            if fmap[i] % 2 == 0:
                res += fmap[i]
            else:
                res += fmap[i] - 1
                hasOddFrequency = True

        return res + 1 if hasOddFrequency else res
