class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        prod = 1
        res = 0
        
        left = 0
        for right, num in enumerate(nums):
            prod *= num
            while prod >= k:
                prod /= nums[left]
                left += 1
            res += right - left + 1
        return res
