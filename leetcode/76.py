# BruteForce
# TimeComplexity: O(mn)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # count element numbers appears in t
        counts = {}
        for ch in t:
            if ch in counts:
                counts[ch]+=1
            else:
                counts[ch]=1

        def t_in_s(counts_s, start, end):
            for ch in counts:
                if ch not in counts_s or counts_s[ch] < counts[ch]:
                    return False

            return True

        # find minimum window substring
        r = ""
        start, end = 0, len(t)-1
        counts_s = {}
        for ch in s[start:end+1]:
            if ch in counts_s:
                counts_s[ch]+=1
            else:
                counts_s[ch]=1
        S = len(s)
        while start < S and end < S:
            if t_in_s(counts_s, start, end) == False:
                end += 1
                if end < S:
                    if s[end] in counts_s: counts_s[s[end]]+=1
                    else: counts_s[s[end]] = 1
                continue

            if r=="" or (end-start+1) < len(r):
                r = s[start:end+1]


            # found start, end which contains t
            # make it shorter by moving start
            start +=1
            counts_s[s[start-1]] -= 1

        return r

# Two Pointers, Sliding Window
# TimeComplexity: O(n)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        left=start=end=0
        
        # 오른쪽 포인터 이동
        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1
            
            # 필요 문자가 0이면 왼쪽 포인터 이동 판단
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]]+=1
                    left+=1
                
                if not end or right - left <= end - start:
                    start, end = left, right
                    
                need[s[left]] +=1
                missing +=1
                left +=1
            
        return s[start:end]
