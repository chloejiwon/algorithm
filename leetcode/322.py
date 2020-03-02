# 322. Coin Change
# Solution 1 - wrong answer 
# not valid when we don't need the biggest number to be divided first
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
       	coins = sorted(coins,reverse=True)
	count = 0
	for coin in coins : 
		if amount//coin >= 1:
			count += amount//coin
			amount = amount % coin
	if amount != 0:
		return -1
	else:
		return count

# Solution 2 - Time Limit Exceeded
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
	dp = [float('inf')] * (amount +1)
	dp[0] = 0
	
	for coin in coins:
		for x in range(coin, amount+1):
			min = float('inf')
			i,rem = 0, x
			while (rem-coin*i)>=0:
				if min > dp[rem-coin*i] + i:
					min = dp[rem-coin*i]+i
				i+=1
			dp[x] = min
	if dp[amount] != float('inf'):
		return dp[amount]
	else:
		return -1

# Solution 3 - Accepted
#  
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount +1)
        dp[0] = 0

        for coin in coins:
                for x in range(coin, amount+1):
                        dp[x] = min(dp[x], dp[x-coin]+1)
        if dp[amount] != float('inf'):
                return dp[amount]
        else:
                return -1


