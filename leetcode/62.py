# 62. Unique Paths
# Solution 1
# Time Complexity : O(m*n)
# Using dp, dp[i][j] = dp[i-1][j]+dp[i][j]
# b/c it is always unique path 

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
     	dp = []
	# Making dp table
	for i in range(m):
		tmp = []
		# Initialization
		for j in range(n): 
			if i == 0 :
				tmp.append(1)
			elif j == 0 :
				tmp.append(1)
			else : 
				tmp.append(0)
		dp.append(tmp)
        
	for i in range(1,n):
            for j in range(1,m):
		dp[i][j] = dp[i-1][j]+dp[i][j-1]
	return dp[n-1][m-1]


