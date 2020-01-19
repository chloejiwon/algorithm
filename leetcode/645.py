class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [sum(nums)-sum(set(nums)), sum(range(1,len(nums)+1))-sum(set(nums))]
