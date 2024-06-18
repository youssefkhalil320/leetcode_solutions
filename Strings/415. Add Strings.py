class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        total = []
        rem = 0

        if len(num1) < len(num2):
            num1 = "0" * (len(num2) - len(num1)) + num1
        elif len(num1) > len(num2):
            num2 = "0" * (len(num1) - len(num2)) + num2

        for i in range(len(num1) - 1, -1, -1):
            num = rem + (ord(num1[i]) - ord('0')) + (ord(num2[i]) - ord('0'))
            rem = num // 10
            total.append(str(num % 10))

        if rem:
            total.append(str(rem))

        return ''.join(total[::-1])
