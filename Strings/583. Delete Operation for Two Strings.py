class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # Ensure word1 is the shorter one to optimize space
        if m < n:
            word1, word2 = word2, word1
            m, n = n, m

        # Only two rows needed
        previous = [0] * (n + 1)
        current = [0] * (n + 1)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    current[j] = 1 + previous[j - 1]
                else:
                    current[j] = max(previous[j], current[j - 1])
            previous, current = current, previous

        lcs_length = previous[n]
        return m + n - 2 * lcs_length
