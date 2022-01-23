class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s:
            return 0
        
        # sort greed factor and size of cookies in descending order
        g.sort(reverse=True)
        s.sort(reverse=True)
        
        # count content children
        child = 0
        j = 0
        for f in g:
            if j < len(s) and f <= s[j]:
                child += 1
                j+=1
        
        return child
        
        
