class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        l = 0
        res = 0
        freq = Counter()
        for r in range(len(s)):
            freq[s[r]] += 1        
            while freq['0'] > k and freq['1'] > k:
                freq[s[l]] -= 1
                l += 1
            res += r - l + 1            
        return res

