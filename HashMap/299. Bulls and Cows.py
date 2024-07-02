class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # Initialize bulls and cows counts
        bulls = 0
        cows = 0

        # Counter to keep track of the numbers in secret and guess
        secret_counter = defaultdict(int)
        guess_counter = defaultdict(int)

        # First pass to count bulls
        for idx in range(len(secret)):
            if secret[idx] == guess[idx]:
                bulls += 1
            else:
                secret_counter[secret[idx]] += 1
                guess_counter[guess[idx]] += 1

        # Second pass to count cows
        for char in guess_counter:
            if char in secret_counter:
                cows += min(secret_counter[char], guess_counter[char])

        return f"{bulls}A{cows}B"
