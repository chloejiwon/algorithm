class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1: return 0
        
        left = 0
        right = nums[0]
        jump = 1
        while right < len(nums)-1:
            nxt = max(nums[i] + i for i in range(left, right+1))
            left = right
            right = nxt
            jump += 1
            
        return jump
