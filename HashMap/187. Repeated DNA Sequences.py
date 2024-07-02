class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        output = []
        smap = defaultdict(int)
        for i in range(len(s)-9):
            sub = s[i:i+10]
            smap[sub] += 1
            if smap[sub] == 2:
                output.append(sub)

        return output
