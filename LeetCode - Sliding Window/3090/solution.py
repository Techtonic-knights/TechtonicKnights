class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        freq = Counter()
        for r in range(len(s)):
            freq[s[r]] += 1          
            while freq[s[r]] > 2:
                freq[s[l]] -= 1
                l += 1          
            max_len = max(max_len, r - l + 1)   
        return max_len
