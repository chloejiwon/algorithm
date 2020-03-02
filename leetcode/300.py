# 300.  Longest Increasing Subsequence
# Solution 1 - Wrong answer 
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
	# dp table create
	cnt = len(nums)
        dp = [[0]*2 for i in range(cnt)]
	
	for i,num in enumerate(nums):
		if i > 0:
			if nums[i-1] < num : 
				# increasing
				dp[i][0] = max(dp[i-1][0], dp[i-1][1])
				dp[i][1] = dp[i-1][1]+1
			else :
				# decreasing
				dp[i][0] = max(dp[i-1][0], dp[i-1][1])
				dp[i][1] = dp[i-1][0] + 1
		else :
			dp[i][0], dp[i][1] = 0,1
	return max(dp[cnt-1][0], dp[cnt-1][1])

# Solution 2 

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
	isIncluded,cnt = False,len(nums)
	if cnt == 0:
		return 0
	dp = [0] * cnt
	for i,num in enumerate(nums):
		if i == 0:
			dp[0] = 1
			isIncluded = True
		else :
			if nums[i-1] < num :
				# increasing
				if isIncluded :
					dp[i] = dp[i-1]+1
				else :
					if dp[i-1] > 2:
						isIncluded = False
						dp = dp[i-1]
					else :
						isIncluded = True
						dp = 2
			else : 
				# decreasing
				isIncluded = False
				dp[i] = dp[i-1]
	return dp[cnt-1]
