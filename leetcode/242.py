# 242. Valid Anagram
"""
Solution 1 : Brute force
- Make dicts for s and t, where key = alphabet, value = count
- If two dicts are the same, return True. else False
"""
def isAnagram( s, t):
	"""
	:type s: str
	:type t: str
	:rtype: bool
	"""
	dicS,dicT = {},{}
	if len(s) != len(t):
		return False

	for i,j in zip(s,t):
		if i in dicS:
			dicS[i]+=1
		else:
			dicS[i]=1
		if j in dicT:
			dicT[j]+=1
		else:
			dicT[j]=1
	if dicS == dicT : 
		return True
	else :
		return False
	
s = "anagram"
t = "nagaram"
print isAnagram(s,t)

s = "rat"
t = "car"
print isAnagram(s,t)
