from collections import Counter


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        total = 0
        count = Counter(words)
        words = set(words)

        def isSubString(word):
            word_ptr = 0
            s_ptr = 0
            matched = 0

            while word_ptr < len(word) and s_ptr < len(s):
                if word[word_ptr] == s[s_ptr]:
                    word_ptr += 1
                    matched += 1
                s_ptr += 1

            return 1 if matched == len(word) else 0

        for word in words:
            total += isSubString(word) * count[word]

        return total
