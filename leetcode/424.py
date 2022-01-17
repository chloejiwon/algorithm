# TimeComplexty: O(kn) but k <= 26
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        S = len(s)
        max_length = min(S, k + 1)
        count = {}
        while left < (S - k):
            if count == {}:
                count = collections.Counter(s[left:left + k + 1])
                right = left+k+1
            else:
                if right < S: count[s[right]] += 1
                right += 1
            
            while right - left - sorted(count.values(), reverse=True)[0] <= k and right <= S:
                if right < S: count[s[right]] += 1
                right += 1
                
            max_length = max(max_length, right-left-1)

            count[s[left]]-=1
            if count[s[left]] == 0: count.pop(s[left])
            left+=1
        return max_length 
