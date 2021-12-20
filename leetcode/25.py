# Solution 1 - Deque
#
# Time Comlexity: O(n)
# Space Complextiy: O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        q = collections.deque()
        
        for elem in s:
            elem = elem.lower()
            if (elem >= 'a' and elem <= 'z') or (elem >= '0' and elem <= '9'):
                q.append(elem)
        
        while q and len(q) > 1:
            if q.popleft() != q.pop():
                return False
        
            
        return True


# Solution 2 - Slicing
#
# Time Complexity: < O(n)
# Space Complexity: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        
        return s == s[::-1]
