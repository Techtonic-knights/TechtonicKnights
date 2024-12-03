class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        number = str(num)
        n = len(number)
        current_num = int(number[:k])
        cnt = 0
        tens_power = 10 ** (k-1)

        for i in range(n-k+1):
            if current_num!=0 and num % current_num == 0:
                cnt += 1
            
            if i+k < n:
                rem_ele = (current_num % tens_power) * 10
                next_ele = int(number[i+k])
                current_num = rem_ele + next_ele
        return cnt
