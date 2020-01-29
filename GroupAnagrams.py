# Group Anagrams
# Medium - Array and strings
# Given an array of strings, group anagrams together.
import collections
def groupAnagrams(strs):
	res, idx = [],[]
	cnt = 0
	for i in range(len(strs)):
		if i in idx:
			continue
		res.append([])
		tmp = collections.Counter(strs[i])
		for j in range(i, len(strs),1):
			if j not in idx:
				tmp2 = collections.Counter(strs[j])
				if tmp == tmp2:
					idx.append(j)
					res[cnt].append(strs[j])
		cnt+=1	
	return res	

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print groupAnagrams(strs)
