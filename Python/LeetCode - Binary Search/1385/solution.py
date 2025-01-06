class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        cnt = 0
        arr2.sort()

        def binary_search(number):
            l, r = 0, len(arr2) - 1
            while l <= r:
                mid = (l+r) // 2
                if abs(number - arr2[mid]) <= d:
                    return False
                elif arr2[mid] < number:
                    l = mid + 1
                else:
                    r = mid - 1
            return True

        for number in arr1:
            if binary_search(number):
                cnt += 1
        return cnt
