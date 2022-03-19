import collections
def lengthOfLongestSubstring(s: str) -> int:
        i, j = 0, 0
        res = 0
        counter = collections.Counter()
        more_than_once = -1
        while j < len(s):
            counter[s[j]] += 1
            if counter[s[j]] > 1: more_than_once = j
            j += 1
            
            if more_than_once == -1:
                res = max(res, j - i)
            
            while more_than_once != -1:
                counter[s[i]] -= 1
                if s[more_than_once] == s[i]: more_than_once = -1
                i += 1
                
        return res

print(lengthOfLongestSubstring("abcabcbb") == 3)
print(lengthOfLongestSubstring("bbbbb") == 1)
print(lengthOfLongestSubstring("pwwkew") == 3)
