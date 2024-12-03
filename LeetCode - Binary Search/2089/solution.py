class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()

        def binary_search(t, find_first):
            l, r = 0, len(nums)-1
            res = -1
            while l <= r:
                mid = (l+r)//2
                if(nums[mid] == t):
                    res = mid
                    if find_first:
                        r = mid - 1
                    else:
                        l = mid + 1
                elif nums[mid] < t:
                    l = mid + 1
                else:
                    r = mid - 1
            return res
        
        left = binary_search(target, find_first=True)
        if left == -1:
            return []
        
        right = binary_search(target, find_first=False)
        return list(range(left, right+1))
