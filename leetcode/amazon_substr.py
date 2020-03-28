# Amazon OA 2019 : Substrings of size K with K distinct chars

# Given a string s and an int k, return all unique substr of s
# of size k with k distinct chars.

# 0 <= k <= 26
# input string consists of only lowercase English letters.

##############################
# Input: s = "abcabc", k = 3
# Output: ["abc", "bca", "cab"]
##############################

def unique_substr(s, k):
    res = []
    i = 0
    while i + k < len(s):
        if s[i:i+k] not in set(res):
            # if not distinct char, skip
            m = {}
            is_distinct = True
            for j in range(i,i+k):
                if s[j] not in m :
                    m[s[j]] = 1
                else :
                    is_distinct = False
            if is_distinct :
                res.append(s[i:i+k])
        i += 1

    return res

# testcase
s = "awaglknagawunagwkwagl"
k = 4
print unique_substr(s,k)