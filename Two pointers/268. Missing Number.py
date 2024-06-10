class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # Calculate the expected sum of numbers from 0 to n
        expected_sum = n * (n + 1) / 2
        # Calculate the actual sum of the given numbers
        actual_sum = sum(nums)
        # The difference between the expected sum and the actual sum is the missing number
        return int(expected_sum - actual_sum)
