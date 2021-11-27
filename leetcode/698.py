"""
Time Complexity: O(k*2^n)
"""
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sums = sum(nums)
        if sums % k != 0:
            return False
        N = len(nums)
        used = [False] * N
        target = sums / k
        
        def backtrack(i, k, subsetSum):
            if k == 0:
                return True
            if subsetSum == target:
                return backtrack(0, k-1, 0)
            
            for j in range(i, N):
                if used[j] or nums[j] + subsetSum > target:
                    continue
                used[j] = True
                if backtrack(j+1, k, subsetSum + nums[j]):
                    return True
                used[j] = False
            return False
        
        return backtrack(0, k, 0)
