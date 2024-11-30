class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for i in range(len(columnTitle)):
            char_val = ord(columnTitle[i]) - ord('A') + 1
            power_val = 26 ** (len(columnTitle) - 1 - i)
            res += power_val * char_val
        return res
