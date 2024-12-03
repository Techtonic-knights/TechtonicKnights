class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        subarray_freq = Counter(nums[:k])
        n = len(nums)
        result = []

        for i in range(n-k+1):
            freq_items = sorted(subarray_freq.items(), key=lambda item: (item[1], item[0]), reverse = True)
            top_x_freq = freq_items[:x]
            x_sum = sum(value * count for value, count in top_x_freq)
            result.append(x_sum)

            if i+k < n:
                prev_ele = nums[i]
                subarray_freq[prev_ele] -= 1

                next_ele = nums[i+k]
                subarray_freq[next_ele] += 1
        return result
