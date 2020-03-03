"""
Solution - Store(memoize)
def fib(n,memo):
	if memo[n]!=float('-inf'):
		return memo[n]
	if n<=1:
		result = n
	else :
		result = fib(n-1,memo) + fib(n-2,memo)
	memo[n] = result
	return result
"""

# Solution - Bottom up
def fib(n):
	# Dp table initialize
	dp = [float('-inf')] * (n+1)
	dp[0],dp[1] = 0,1
	
	for i in range(2,n+1):
		dp[i] = dp[i-1]+dp[i-2]
	
	return dp[n]

print fib(5)
