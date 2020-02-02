#Given a string, find the length of the longest substring without repeating characters.
def lengthOfLongestSubstring(s):
	# Sliding Window FInd the maximum length of window
	if not s:
		return 0
	window_size = 1
	for i in range(len(s)):
		for j in range(len(s), i+1, -1):
			if j-i <= window_size :
				break
			if len(set(s[i:j])) == j-i:
				if window_size < j-i :
					window_size = j-i
				break
	return window_size			

s = "abcabcbb"
print lengthOfLongestSubstring(s)

s = "bbbbb"
print lengthOfLongestSubstring(s)

s = "pwwkew"
print lengthOfLongestSubstring(s)

s = "au"
print lengthOfLongestSubstring(s)

s = ""
print lengthOfLongestSubstring(s)
