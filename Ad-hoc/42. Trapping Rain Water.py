class Solution:
    def trap(self, height: List[int]) -> int:
        max_idx = 0
        left_max = 0
        right_max = 0
        ans = 0

        for i in range(len(height)):
            if height[i] > height[max_idx]:
                max_idx = i

        for i in range(max_idx):
            left_max = max(left_max, height[i])
            ans += left_max - height[i]

        for i in range(len(height) - 1, max_idx, -1):
            right_max = max(right_max, height[i])
            ans += right_max - height[i]

        return ans
