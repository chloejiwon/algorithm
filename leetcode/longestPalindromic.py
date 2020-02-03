# Given a string s, find the longest palindromic substr in s.
# May assume that the maximum length of s is 1000
# Solution 1 : Brute Force!!
"""
def longestPalindrome(s):
	def isPalindrome(substr):
		l,r = 0, len(substr)-1
		while l<=r:
			if substr[l] != substr[r]:
				return False
			l+=1
			r-=1
		return True
	if not s: return ""
	res, N, maxLen = "", len(s), float('-inf')
	if isPalindrome(s) == True:
		return s
	for i in range(N):
		for j in range(N-1, i-1, -1):
			if isPalindrome(s[i:j+1]) and j-i+1 > maxLen:
				maxLen = j-1+1
				res = s[i:j+1]
				break
	return res
"""
# Soltuion 2 
# Time Complexity : O(N^2)
def longestPalindrome(s):
	def findPalindrome(l,r):
		while l >=0 and r<len(s) and l<=r:
			if s[l] != s[r]:
				break
			l-=1
			r+=1
		return s[l+1:r]
	if not s : return ""
	res , N, maxLen = "", len(s), float('-inf')
	for i in range(N):
		# find palindrome s[i] == middle / s[i] = left 
		tmp = findPalindrome(i,i)
		if len(tmp) > maxLen:
			maxLen = len(tmp)
			res = tmp
		tmp = findPalindrome(i,i+1)
		if len(tmp) > maxLen:
			maxLen = len(tmp)
			res = tmp
	return res
s = "aaa"
print longestPalindrome(s)

s = "babad"
print longestPalindrome(s)

s = "cbbd"
print longestPalindrome(s)
