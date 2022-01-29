def climb_stairs(n: int) -> int:
	dp = [0,1,2]
	for i in range(3, n+1):
		dp.append(dp[i-1] + dp[i-2])
	
	return dp[n]
	
