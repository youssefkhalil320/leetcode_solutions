class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        cur, res = 1, 1
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                continue
            if nums[i-1]+1 == nums[i]:
                cur += 1
                res = max(res, cur)
            else:
                cur = 1
        return res
