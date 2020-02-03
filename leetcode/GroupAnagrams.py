# Group Anagrams
# Medium - Array and strings
# Given an array of strings, group anagrams together.
import collections
def groupAnagrams(strs):
	ans = collections.defaultdict(list)
	for s in strs:
		ans[tuple(sorted(s))].append(s)
	return ans.values()
