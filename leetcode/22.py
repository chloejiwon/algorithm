# 22. Generate Parentheses

# Solution 1 
# Make like a tree and Use DFS. 
# Time Complexity : O(nlogn) -  beat 81.12% 
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(num,str,left,r):
                # num = '(' left parenthesis number wating to be pair!
                # left = '(' nums left
                if num == 0 and left == 0:
                        r.append(str)
                        return str
                if num > 0 :
                        generate(num-1,str+')',left,r)
                        if left > 0:
                                generate(num+1, str+'(', left-1,r)
                if num == 0 and left > 0 :
                        generate(num+1, str+'(', left-1,r)
        res = []
        generate(0,"",n,res)
        return res
