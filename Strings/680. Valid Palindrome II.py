class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalindrome(s, left, right, num_delete):
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    if num_delete:
                        # Check by removing one character either from the left or right
                        return ispalindrome(s, left + 1, right, num_delete - 1) or ispalindrome(s, left, right - 1, num_delete - 1)
                    else:
                        return False
            return True

        return ispalindrome(s, 0, len(s) - 1, 1)
