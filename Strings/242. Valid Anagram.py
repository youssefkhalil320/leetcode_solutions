class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = defaultdict(int)
        t_map = defaultdict(int)

        for idx in range(len(s)):
            s_map[s[idx]] += 1
            t_map[t[idx]] += 1

        for key in s_map:
            if s_map[key] != t_map[key]:
                return False

        return True
