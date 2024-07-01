class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]  # Initialize with the first element

        for num in nums[1:]:  # Start from the second element
            if abs(num) < abs(closest):
                closest = num
            elif abs(num) == abs(closest) and num > closest:
                closest = num

        return closest
