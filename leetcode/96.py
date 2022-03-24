def numTrees(n: int) -> int:
	if n <= 2:
		return n
	dp = [0]*(n+1)
	dp[0] = 1
	dp[1] = 1
	dp[2] = 2
	for i in range(3, n+1):
		for j in range(1, i+1):
			dp[i] += dp[i-j] * dp[j-1]

	return dp[n] 

print(numTrees(3) == 5)
print(numTrees(5) == 42)
