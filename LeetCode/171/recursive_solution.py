class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        def recursion_helper(title, idx):
            if idx >= len(title):
                return 0
            char_val = ord(title[idx]) - ord('A') + 1
            power_val = 26 ** (len(title) - 1 - idx)
            return (power_val * char_val) + recursion_helper(title, idx+1)
        return recursion_helper(columnTitle, 0)
