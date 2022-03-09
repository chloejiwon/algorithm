def word_break(s: str, word_dict: [str]) -> bool:
	ok = [False] * (len(s)+1)
	ok[0] = True
	for i in range(1, len(s)+1):
		for w in word_dict:
			if i-len(w)>=0 and s[i-len(w):i] == w:
				ok[i] = ok[i-len(w)]
			if ok[i]:
				break
	return ok[-1]

#######
print(word_break("catsandog", ["cats","dog","sand","and","cat"]))
print(word_break("applepenapple", ["apple","pen"]))
print(word_break("leetcode", ["leet","code"]))
print(word_break("a", ["c","bbbbb"]))
