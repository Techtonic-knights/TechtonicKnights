class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n= len(nums)

        def binary_search(target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            return l
        
        for number in range(1, n+1):
            idx = binary_search(number)
            cnt = n - idx
            if cnt == number:
                return number
        return -1
        
            
        
