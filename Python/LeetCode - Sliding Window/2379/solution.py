class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        sub_array_freq = Counter(blocks[:k])
        min_cnt = float('inf')
        n = len(blocks)
        for i in range(n - k + 1):
            cnt = sub_array_freq['W']
            min_cnt = min(cnt, min_cnt)

            if i+k < n:
                prev_ele = blocks[i]
                sub_array_freq[prev_ele] -= 1
                
                ele_to_include = blocks[i+k]
                sub_array_freq[ele_to_include] += 1
        return min_cnt
