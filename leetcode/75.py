# 75. Sort Colors

# Solution 1
# Using Counting sort : beat 96.93%
# Time Complexity : O(n)
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
	n0,n1,n2 = 0,0,0
        for n in nums:
		if n == 0: 
			n0+=1
		elif n ==1:
			n1+=1
		elif n==2:
			n2+=1
	for n in range(len(nums)):
		if n>=0 and n<n0:
			nums[n] = 0
		elif n>=n0 and n<(n0+n1):
			nums[n] = 1
		elif n>=(n0+n1) and n<(n0+n1+n2):
			nums[n] = 2
