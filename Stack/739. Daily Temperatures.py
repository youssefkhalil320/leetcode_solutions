from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                stacki = stack.pop()
                res[stacki] = i - stacki
            stack.append(i)

        return res
